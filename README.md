<!-- llm-readme-management spec=1 commit=c9611e16bbfc4551c8993e4fbb1073a878ba2ede template=default model=qwen3.8-27b-q4 digest=598d66067ca0 generated=2026-10-12T12:18:12Z -->
<a href="https://hauke.cloud" target="_blank"><img src="https://img.shields.io/badge/home-hauke.cloud-brightgreen" alt="hauke.cloud" style="display: block;" /></a>
<a href="https://github.com/hauke-cloud" target="_blank"><img src="https://img.shields.io/badge/github-hauke.cloud-blue" alt="hauke.cloud Github Organisation" style="display: block;" /></a>
<a href="https://github.com/hauke-cloud/llm-readme-management" target="_blank"><img src="https://img.shields.io/badge/template-default-orange" alt="Repository type - default" style="display: block;" /></a>


# Smee


<img src="https://raw.githubusercontent.com/hauke-cloud/.github/main/resources/img/organisation-logo-small.png" alt="hauke.cloud logo" width="109" height="123" align="right">


<llm header>

This repository packages and publishes the `smee` CLI, a bash script that launches preconfigured containerized working environments via Docker or Podman. If you are a developer on Debian, Fedora, RHEL, CentOS, or Arch Linux who wants a single command to start a container with your project mounted, the GPG-signed DEB, RPM, and AUR packages here are for you.

</llm>


## :book: Description

<llm description>

`smee` is a bash CLI that starts a preconfigured containerized working environment from a single sourced config file. Rather than hand-assembling `docker run` or `podman run` commands with the right flags for ports, volume mounts, environment variables, and user mapping, you write a small `./.smee` file (or point `SMEE_FILE` at one) and run `smee run`. The script resolves the image—build from a local Dockerfile or pull by name—assembles the full container invocation, and prefers Docker, falling back to Podman.

This repository is the packaging and CI home for that CLI. It holds the installable payload (`src/usr/bin/smee`, `src/etc/smee/default.conf`) and the GitHub Actions workflows that build GPG-signed DEB and RPM packages, publish them to GitHub Pages at `hauke-cloud.github.io/smee/`, and open a draft GitHub Release on every tag. An AUR workflow is also present for Arch Linux.

- `smee init` seeds a local `./.smee` from the shipped defaults.
- `smee run` builds or pulls an image, then launches the container with ports, mounts, env vars, entrypoint override, and (Podman-only) UID/GID mapping.
- CI produces signed `amd64` DEB and `x86_64` RPM packages with APT/RPM repo metadata, deployed to GitHub Pages.

</llm>


## 🚀 Getting started

<llm getting_started hint="Assume nothing about the ecosystem beyond what the analysis names. If the repository has no build step, say what a reader does with it instead.">

1. Clone the repository.

```bash
git clone https://github.com/hauke-cloud/smee.git
cd smee
```

2. Add the APT signing key and repository source list.

```bash
sudo apt-get install ca-certificates curl
sudo curl -fsSL https://hauke-cloud.github.io/smee/apt/hauke-cloud.asc -o /etc/apt/keyr

</llm>


## :airplane: Usage

<llm usage>

After installing the `smee` package, you work with it from any directory where you want a containerized working environment.

**Initialize a config file.** Run `smee init` in your project directory. This copies `/etc/smee/default.conf` to `./.smee`. The command refuses to overwrite a file that already exists.

```bash
smee init
```

**Run a container.** `smee run` (or simply `smee`, since `run` is the default sub-command) sources `./.smee` and assembles a `docker run` or `podman run` call. The shipped defaults set `SMEE_BUILD=1` and `SMEE_BUILD_PATH=deploy/smee/Dockerfile`, so a first run expects a local Dockerfile. To pull a pre-built image instead, edit `./.smee`:

```bash
SMEE_BUILD=0
SMEE_PULL=1
SMEE_IMAGE=busybox
SMEE_COMMAND=sh
```

Then start the environment:

```bash
smee run
```

**Point at a different config.** Use `-s` / `--smee-file` to source an alternate file, or set the `SMEE_FILE` environment variable. A `${SMEE_FILE}.custom` file takes precedence over `${SMEE_FILE}` when both exist.

```bash
smee -s ./ci.smee run
```

</llm>


## 📄 License

This Project is licensed under the GNU General Public License v3.0

- see the [LICENSE](LICENSE) file for details.


## :coffee: Contributing

To become a contributor, please check out the [CONTRIBUTING](CONTRIBUTING.md) file.


## :email: Contact

For any inquiries or support requests, please open an issue in this
repository or contact us at [contact@hauke.cloud](mailto:contact@hauke.cloud).
