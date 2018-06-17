Run TWS in Docker.

## Updating TWS

Configure TWS_SYNC_CONF to 'yes'
Launch an instance of ib-docker
Copy TWS configuration files into /tmp/tws. This can be done automatically:
* Mount /tmp/tws to a local directory
* Login to TWS via VNC
* Restart TWS by exiting the application. IBController will automatically relaunch the application.
* The configuration files for the currently logged in account will be copied by the launch script.
Terminate the ib-docker instance and remove the container
Modify the section named "ApiSettings" for your particular needs.