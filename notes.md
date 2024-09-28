## PipeWire Low Volumn
https://wiki.archlinux.org/title/PipeWire#Low_volume

After replacing PulseAudio with Pipewire, sound may work fine, but after a reboot, the volume becomes intolerably low.

Open alsamixer, use F6 to select the proper soundcard, and make sure the ALSA volumes are at 100%. alsactl should maintain this setting after reboot.

## NetworkManager iwd backend
https://wiki.archlinux.org/title/NetworkManager#Using_iwd_as_the_Wi-Fi_backend
`wifi_backend.conf`
```
[device]
wifi.backend=iwd
```
