<p align="center">
  <img src="resources/img/logo.png" alt="repository logo" width="20%" height="20%">
</p>

<a href="https://hauke.cloud" target="_blank"><img src="https://img.shields.io/badge/home-hauke.cloud-brightgreen" alt="hauke.cloud" style="display: block;" /></a>
<a href="https://github.com/hauke-cloud" target="_blank"><img src="https://img.shields.io/badge/github-hauke.cloud-blue" alt="hauke.cloud Github Organisation" style="display: block;" /></a>
<a href="https://github.com/hauke-cloud/readme-management" target="_blank"><img src="https://img.shields.io/badge/template-apt.rpm-orange" alt="Repository type - apt-rpm" style="display: block;" /></a>

# Smee - OCI Tooling Images

<img src="https://raw.githubusercontent.com/hauke-cloud/.github/main/resources/img/organisation-logo-small.png" alt="hauke.cloud logo" width="109" height="123" align="right">

Every ship needs Smee (even Container ships).
Smee provides easy to spin up working environments by using OCI technologies.

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
sudo curl -fsSL https://hauke-cloud.github.io/smee/apt/hauke-cloud.asc -o /etc/apt/keyrings/smee.asc
sudo chmod a+r /etc/apt/keyrings/smee.asc
```

Now you can add the repository to your sources list

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/smee.asc] https://hauke-cloud.github.io/smee/apt stable main" | \
  sudo tee /etc/apt/sources.list.d/smee.list > /dev/null
```

And finally update the apt cache and install the package

```bash
sudo apt-get update
sudo apt-get install smee
```

### Installation via RPM

First you need to create a repo file:

```bash
cat >/etc/yum.repos.d/smee.repo <<EOF
[smee]
name=smee
baseurl=https://hauke-cloud.github.io/smee/rpm
enabled=1
repo_gpgcheck=1
type=rpm
gpgcheck=1
gpgkey=https://hauke-cloud.github.io/smee/rpm/RPM-GPG-KEY
EOF
```

Now you can update your dnf cache

```bash
sudo dnf update
```

Finally you can install the package

```bash
sudo dnf install smee
```

## :airplane: Usage

### Provide settings via .env file

Smee allows to provide a `.env` file to store environment variables.
Environment variables are key-value pairs that configure the behavior of the application without changing the source code.

### 1. Create a `.env` File

In the root directory of the project, create a new file named `.env`:

```bash
touch .env
```

### 2. Add Variables in `KEY=VALUE` Format

Each line should contain one variable definition, with no spaces around the `=`:

```dotenv
# Server configuration
PORT=3000
HOST=127.0.0.1

# Database credentials
DB_HOST=localhost
DB_PORT=5432
DB_USER=myuser
DB_PASSWORD=supersecret

# API keys
API_KEY=abcd1234
```

**Rules:**

- Keys should be **uppercase** and descriptive.
- No quotes are required unless the value contains spaces.
- Lines starting with `#` are comments and will be ignored.

Example with spaces and special characters:

```dotenv
GREETING="Hello World"
PASSWORD="p@ss word!"
```

### 3. Keep `.env` Out of Version Control

Sensitive data (like passwords or API keys) should **never** be committed to Git.
Add `.env` to your `.gitignore`:

```gitignore
.env
```

### 4. Loading the `.env` File

Set the Smee env file setting in ```.smee```.

```dotenv
SMEE_ENV_FILE=".env"
```

### Provide settings via .envrc file

Similar to the env file Smee allows to provide a `.envrc` file to store environment variables.
The difference between env files and envrc files is that envrc allows not only simple "key=value" sharing but also the use of commands and many features of bash.

### 1. Create a `.envrc` File

In the root directory of the project, create a new file named `.envrc`:

```bash
touch .envrc
```

### 2. Add variables the bash way like `export KEY=VALUE`

Each line should contain one variable definition:

```dotenv
# Server configuration
export PORT=3000
export HOST=$(hostname -I | cut -d' ' -f 1)
```

**Rules:**

- Keys should be **uppercase** and descriptive.
- No quotes are required unless the value contains spaces.
- Lines starting with `#` are comments and will be ignored.

### 3. Loading the `.envrc` File

Set the Smee env file setting in ```.smee```.

```dotenv
SMEE_ENV_RCFILE=".envrc"
```

## 📄 License

This Project is licensed under the GNU General Public License v3.0

- see the [LICENSE](LICENSE) file for details.

## :coffee: Contributing

To become a contributor, please check out the [CONTRIBUTING](CONTRIBUTING.md) file.

## :email: Contact

For any inquiries or support requests, please open an issue in this
repository or contact us at [contact@hauke.cloud](mailto:contact@hauke.cloud).
