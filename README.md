

<a href="https://hauke.cloud" target="_blank"><img src="https://img.shields.io/badge/home-hauke.cloud-brightgreen" alt="hauke.cloud" style="display: block;" /></a>
<a href="https://github.com/hauke-cloud" target="_blank"><img src="https://img.shields.io/badge/github-hauke.cloud-blue" alt="hauke.cloud Github Organisation" style="display: block;" /></a>
<a href="https://github.com/hauke-cloud/readme-management" target="_blank"><img src="https://img.shields.io/badge/template-apt-rpm-orange" alt="Repository type - apt-rpm" style="display: block;" /></a>


# Every container ship needs a Smee


<img src="https://raw.githubusercontent.com/hauke-cloud/.github/main/resources/img/organisation-logo-small.png" alt="hauke.cloud logo" width="109" height="123" align="right">


Smee provides easy to spin up working environments by using open container technologies.

What you can do with it:
- Describe your tooling / working environment in Dockerfiles
- Desscribe your mounts, static variables, etc via Smee config file
- Spin up a fresh working environment via simple execute ```smee```





## 👨🏻‍🔧 Installation
### Installation via APT
First you need to download the GPG we are using to sign out repository
```bash
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://hauke-cloud.github.io/smee/hauke-cloud.asc -o /etc/apt/keyrings/smee.asc
sudo chmod a+r /etc/apt/keyrings/smee.asc
```

Now you can add the repository to your sources list
```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/smee.asc] https://hauke-cloud.github.io/smee/apt main stable" | \
  sudo tee /etc/apt/sources.list.d/smee.list > /dev/null
```

And finally update the apt cache and install the package
```bash
apt-get update
apt-get install smee
```

### Installation via RPM
First you need to create a repo file:
```bash
cat >/etc/yum.repos.d/smee.repo <<EOF
[smee]
name=smee
baseurl=https://hauke-cloud.github.io/smee
enabled=1
repo_gpgcheck=1
type=rpm
gpgcheck=1
gpgkey=https://hauke-cloud.github.io/smee/RPM-GPG-KEY
EOF
```

Now you can update your dnf cache
```bash
sudo dnf update
```



## 📄 License

This Project is licensed under the GNU General Public License v3.0

- see the [LICENSE](LICENSE) file for details.


## :coffee: Contributing

To become a contributor, please check out the [CONTRIBUTING](CONTRIBUTING.md) file.


## :email: Contact

For any inquiries or support requests, please open an issue in this
repository or contact us at [contact@hauke.cloud](mailto:contact@hauke.cloud).

