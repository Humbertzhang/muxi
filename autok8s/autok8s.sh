Test() {
    echo  "\033[41;36m Exec: $* ... \033[0m"
    $*
    if [ $? != 0 ]
    then
        echo "\033[41;33m Failed: $*! \033[0m"
        exit 0
    fi
    echo "\033[41;36m Finished! \033[0m"
}

# 关闭防火墙

echo "关闭防火墙"
Test systemctl disable firewalld
Test systemctl stop firewalld
Test sed -i 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/selinux/config
Test echo 1 > /proc/sys/net/bridge/bridge-nf-call-iptables
Test echo 1 > /proc/sys/net/bridge/bridge-nf-call-ip6tables



echo "安装docker 1.12.6"
cat >/etc/yum.repos.d/docker.repo <<EOF
[dockerrepo]
name=Docker Repository
baseurl=https://yum.dockerproject.org/repo/main/centos/7
enabled=1
gpgcheck=1
gpgkey=https://yum.dockerproject.org/gpg
EOF
Test yum makecache
Test yum install docker-engine-1.12.6-1.el7.centos.x86_64
Test systemctl start docker



echo "加速Docker"
Test sudo mkdir -p /etc/docker
sudo tee /etc/docker/daemon.json <<-'EOF'
{
  "registry-mirrors": ["https://sw9esv3f.mirror.aliyuncs.com"]
}
EOF
Test sudo systemctl daemon-reload
Test sudo systemctl restart docker

echo "安装k8s套件"
cat >> /etc/yum.repos.d/kubernetes.repo <<EOF
[kubernetes]
name=Kubernetes
baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64/
enabled=1
gpgcheck=0
EOF
Test yum install -y kubernetes-cni-0.5.1-0.x86_64 
Test yum install -y kubelet-1.7.5-0.x86_64 
Test yum install -y kubectl-1.7.5-0.x86_64 
Test yum install -y kubeadm-1.7.5-0.x86_64



echo "拉取k8s镜像"
images=(etcd-amd64:3.0.17 pause-amd64:3.0 kube-proxy-amd64:v1.7.5 kube-scheduler-amd64:v1.7.5 kube-controller-manager-amd64:v1.7.5 kube-apiserver-amd64:v1.7.5 kubernetes-dashboard-amd64:v1.6.1 k8s-dns-sidecar-amd64:1.14.4 k8s-dns-kube-dns-amd64:1.14.4 k8s-dns-dnsmasq-nanny-amd64:1.14.4)
for imageName in ${images[@]} ; do
  Test docker pull mirrorgooglecontainers/$imageName
  Test docker tag mirrorgooglecontainers/$imageName gcr.io/google_containers/$imageName
  Test docker rmi mirrorgooglecontainers/$imageName
done


echo "配置kubelet"
Test cat > /etc/systemd/system/kubelet.service.d/20-pod-infra-image.conf <<EOF
[Service]
Environment="KUBELET_EXTRA_ARGS=--pod-infra-container-image=mirrorgooglecontainers/pause-amd64:3.0"
EOF
Test sed -i 's/cgroup-driver=systemd/cgroup-driver=cgroupfs/g' /etc/systemd/system/kubelet.service.d/10-kubeadm.conf

Test systemctl enable docker
Test systemctl enable kubelet
Test systemctl start docker
Test systemctl start kubelet

echo "初始化集群"
export KUBE_REPO_PREFIX="mirrorgooglecontainers"
export KUBE_ETCD_IMAGE="registry.cn-hangzhou.aliyuncs.com/szss_k8s/etcd-amd64:3.0.17"
Test kubeadm init  --kubernetes-version=v1.7.5 --pod-network-cidr=10.244.0.0/12

echo "配置kubectl的kubeconfig"
mkdir -p $HOME/.kube
cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
chown $(id -u):$(id -g) $HOME/.kube/config

echo "配置flannel"
Test kubectl --namespace kube-system apply -f https://raw.githubusercontent.com/coreos/flannel/v0.8.0/Documentation/kube-flannel-rbac.yml
Test rm -rf kube-flannel.yml 
Test wget https://raw.githubusercontent.com/coreos/flannel/v0.8.0/Documentation/kube-flannel.yml
Test sed -i 's/quay.io\/coreos\/flannel:v0.8.0-amd64/registry.cn-hangzhou.aliyuncs.com\/szss_k8s\/flannel:v0.8.0-amd64/g' ./kube-flannel.yml
Test kubectl --namespace kube-system apply -f ./kube-flannel.yml
