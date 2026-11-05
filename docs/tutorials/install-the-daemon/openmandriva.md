(tutorials-install-the-daemon-openmandriva)=
# Install Snap on OpenMandriva 

OpenMandriva supplies `snapd` in its repositories. It takes two steps to get it going: 

1. Install `snapd`: 

   ```bash
   sudo dnf install snapd
   ```

1. Enable `snapd`: 

   ```bash 
   sudo systemctl enable --now snapd
   ```

## Confinement

AppArmor is not installed by default on OpenMandriva. It takes the same two steps to install and enable it: 

1. Install: 

   ```bash 
   sudo dnf install apparmor
   ```

1. Enable: 

   ```bash 
   sudo systemctl enable apparmor
   ```

Enjoy!
