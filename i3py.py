#!/usr/bin/python3
from i3pystatus import Status
import locale
locale.setlocale(locale.LC_ALL, 'nb_NO.UTF-8')

status = Status(standalone=True)

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock",
                format="%a %d.%m %H:%M",
                interval = 5)

# The battery monitor has many formatting options, see README for details

# This would look like this, when discharging (or charging)
# ↓14.22W 56.15% [77.81%] 2h:41m
# And like this if full:
# =14.22W 100.0% [91.21%]
#
# This would also display a desktop notification (via dbus) if the percentage
# goes below 5 percent while discharging. The block will also color RED.
#status.register("battery",
#                format="{status} [{consumption:.1f}W ]{percentage:.0f}%[ {remaining:%E%hh:%Mm}]",
#    alert=True,
#    alert_percentage=5,
#    status={
#        "DIS": "↓",
#        "CHR": "↑",
#        "FULL": "⚡"
#    },)
#
# # This would look like this:
# # Discharging 6h:51m
# status.register("battery",
#     format="{status} {remaining:%E%hh:%Mm}",
#     alert=True,
#     alert_percentage=5,
#     status={
#         "DIS":  "Discharging",
#         "CHR":  "Charging",
#         "FULL": "Bat full",
#     },)

# Shows the average load of the last minute and the last 5 minutes
# (the default value for format is used)
# status.register("load")

# status.register("cpu_usage", format="CPU: {usage}%")

# Shows your CPU temperature, if you have a Intel CPU
# status.register("temp",
#     format="{temp:.0f}°C",
#     interval=3)


# Displays whether a DHCP client is running
# status.register("runwatch",
#     name="DHCP",
#     path="/var/run/dhclient*.pid",)

# Shows the address and up/down state of eth0. If it is up the address is shown in
# green (the default value of color_up) and the CIDR-address is shown
# (i.e. 10.10.10.42/24).
# If it's down just the interface name (eth0) will be displayed in red
# (defaults of format_down and color_down)
#
# Note: the network module requires PyPI package netifaces
status.register("network",
    interface="em1",
    format_up="{v4cidr}",)

# Has all the options of the normal network and adds some wireless specific things
# like quality and network names.
#
# Note: requires both netifaces and basiciw
# status.register("wireless",
#     interface="wlp2s0",
#     format_up="{essid} {quality:03.0f}%",)

# Shows disk usage of /
# Format:
# 42/128G [86G]
# status.register("disk",
#     path="/tmp",
#     format="{used}M",
#     divisor=1024**2)

# Shows pulseaudio default sink volume
#
# Note: requires libpulseaudio from PyPI
# status.register("backlight",
#     format="☼ {percentage:.0f}%",
#     backlight='intel_backlight')

status.register("pulseaudio",
    format="♪ {volume}%",)

status.run()
