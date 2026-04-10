# asitop (for Apple M5Pro)

Performance monitoring CLI tool for Apple Silicon

![](images/asitop.png)

Note: The source code is specifically modified for Apple M5 Pro (15CPU+16GPU). Since this is the only device I have, there might be some error on different models. For example, the S/P core numbering may be incorrect for other M5 Pro/Max series SoC. 

This repo is forked from the original [asitop](https://github.com/tlkh/asitop), as the author has stopped any support for years, and the legacy version does not work for the latest Apple Silicon SoC. As Apple has changed the naming of CPU core clusters from P/E to S/P, I have also modified the code to support this change. 




1. Keep your source code in a stable location (like ~/Projects/asitop_M5Pro)

2. Install with: 

```shell
  pip install -e ~/Projects/asitop_M5Pro
```

3. Run with: sudo asitop


## What is `asitop`

A Python-based `nvtop`-inspired command line tool for Apple Silicon (aka M1) Macs.

* Utilization info:
  * CPU (E-cluster and P-cluster), GPU
  * Frequency and utilization
  * ANE utilization (measured by power)
* Memory info:
  * RAM and swap, size and usage
  * (Apple removed memory bandwidth from `powermetrics`)
* Power info:
  * CPU power, GPU power (Apple removed package power from `powermetrics`)
  * Chart for CPU/GPU power
  * Peak power, rolling average display

  `asitop` uses the built-in [`powermetrics`](https://www.unix.com/man-page/osx/1/powermetrics/) utility on macOS, which allows access to a variety of hardware performance counters. Note that it requires `sudo` to run due to `powermetrics` needing root access to run. `asitop` is lightweight and has minimal performance impact.

## Installation and Usage

`asitop` is a Python-based command line tool. You need `pip` to download and install `asitop`. macOS already comes with Python, to install `pip`, you can follow an [online guide](https://phoenixnap.com/kb/install-pip-mac). After you install `asitop` via `pip`, you can use it via the Terminal.

```shell
# to enter password before start
# this mode is recommended!
sudo asitop

# it will prompt password on start
asitop

# advanced options
asitop [-h] [--interval INTERVAL] [--color COLOR] [--avg AVG]
optional arguments:
  -h, --help           show this help message and exit
  --interval INTERVAL  Display interval and sampling interval for powermetrics (seconds)
  --color COLOR        Choose display color (0~8)
  --avg AVG            Interval for averaged values (seconds)
```

## How it works

`powermetrics` is used to measure the following:

* CPU/GPU utilization via active residency
* CPU/GPU frequency
* Package/CPU/GPU/ANE energy consumption
* CPU/GPU/Media Total memory bandwidth via the DCS (DRAM Command Scheduler)

[`psutil`](https://github.com/giampaolo/psutil) is used to measure the following:

* memory and swap usage

[`sysctl`](https://developer.apple.com/library/archive/documentation/System/Conceptual/ManPages_iPhoneOS/man3/sysctl.3.html) is used to measure the following:

* CPU name
* CPU core counts

[`system_profiler`](https://ss64.com/osx/system_profiler.html) is used to measure the following:

* GPU core count

Some information is guesstimate and hardcoded as there doesn't seem to be a official source for it on the system:

* CPU/GPU TDP
* CPU/GPU maximum memory bandwidth
* ANE max power
* Media engine max bandwidth

## Why

Because I didn't find something like this online. Also, just curious about stuff.

## Disclaimers

I did this randomly don't blame me if it fried your new MacBook or something.
