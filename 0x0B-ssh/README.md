# 0x0B. SSH

During this project, I got the hang of connecting to servers and working with them using the SSH protocol. I was hands-on with a server that ALX provided.

## Tasks 📃

### 0. Use a private key

[0-use_a_private_key](): Bash script that uses ssh to connect to your server using the private key `~/.ssh/school` with the user `ubuntu`.

Requirements:
- Only use ssh single-character flags.
- You cannot use `-l`.
- You do not need to handle the case of a private key protected by a passphrase.

### 1. Create an SSH key pair

- [1-create_ssh_key_pair](): Bash script that creates an RSA key pair.

Requirements:
- Name of the created private key must be `school`.
- Number of bits in the created key to be created 4096.
- The created key must be protected by the passphrase `betty`.

### 2. Client configuration file

- [2-ssh_config](http://www.hello.com): SSH configuration file that is set up to use the private key `~/.ssh/school` for authentication. Additionally, the configuration is tuned to reject authentication attempts using passwords.
