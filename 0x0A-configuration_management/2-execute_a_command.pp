# Manifest to kill a process named "killmenow"

exec { 'killmenow_process':
  command     => '/usr/bin/pkill -f killmenow',
  refreshonly => true,
}
