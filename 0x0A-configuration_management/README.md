# Configuration management

In this project, I've been learning Puppet, a configuration management tool. I practiced creating files, installing packages, and running commands using Puppet manifest files."

## Tasks 📃

### 1. Create a File
The Puppet manifest file [0-create_a_file.pp]() is designed to create a file named "school" in the `/tmp` directory. The file is configured with specific permissions (0744), ownership (www-data), group (www-data), and contains the content "I love Puppet."

To apply the manifest, use the following command:
```bash
 puppet apply 0-create_a_file.pp
```

### 2. Install a Package (Flask)
The [1-install_a_package.pp]() manifest is crafted to install Flask version 2.1.0 using the pip3 provider. However, if encountering issues with the provider, alternative methods like installing the puppetlabs-python module or using system package managers (apt, yum) are suggested.

To apply the manifest, execute:

```bash
puppet apply 1-install_a_package.pp
```

### Execute a Command (Kill a Process)

For the task of killing a process named "killmenow," the exec resource is employed in the [2-kill_a_process.pp]() manifest. This resource uses the pkill command to terminate the specified process. Ensure proper permissions and execution by running Puppet as needed .

Apply the manifest with

```bash
puppet apply 2-kill_a_process.pp
```
## Additional Notes:

### Running Puppet as Root
If you encounter errors related to permissions, ensure you run Puppet with administrative privileges. Prefix the puppet apply command with sudo:

```bash
sudo puppet apply <manifest_filename>
```
### Checking Puppet Manifests with puppet-lint
To check your Puppet manifests for style and syntax, you can use puppet-lint. Install it using:
```bash
gem install puppet-lint
```
Then, run it on your manifest files:

```bash
puppet-lint <manifest_filename>
```
Fix any error using:
```bash
puppet-lint --fix <manifest_filename>
```