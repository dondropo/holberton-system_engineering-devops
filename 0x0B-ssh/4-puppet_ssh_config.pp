# ssh key configuration with Puppet

file_line { 'ssh identity':
path => '/etc/ssh/ssh_config',
line => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'ssh_key':
path => '/etc/ssh/ssh_config',
line => 'PasswordAuthentication no'
}

