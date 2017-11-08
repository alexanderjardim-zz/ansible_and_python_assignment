Vagrant.configure("2") do |config|

  config.vm.box = "ubuntu/trusty64"

  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
  end

  config.vm.define "ubuntu" do |m|
    m.vm.network "private_network", ip: "172.17.177.21"
    m.vm.provision :ansible_local do |ansible|
      ansible.playbook = "provisioning.yml"
      ansible.verbose = "vvvv"
      ansible.install_mode = "pip"
      ansible.version = "2.4.1.0"
      ansible.extra_vars = {
        docker_package: 'docker.io'
      }
    end
  end

  config.vm.define "centos" do |m|
    m.vm.network "private_network", ip: "172.17.177.22"
    m.vm.box = "centos/7"
    m.vm.provision :ansible_local do |ansible|
      ansible.playbook = "provisioning.yml"
      ansible.verbose = "vvvv"
      ansible.install_mode = "pip"
      ansible.version = "2.4.1.0"
      ansible.extra_vars = {
        docker_package: 'docker'
      }
    end
  end

end
