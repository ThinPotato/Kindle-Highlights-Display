# Kindle-Highlights-Display
This is the software repository for my highlights project. This repo has two parts. The first being a webcrawler that downloads and saves your highlgihts from the amazon website. The second being the software behind the physical display. It chooses a random highlight, uses an API to download additional information (such as book name, author, cover art, etc.) And displays it into a PIL image to be loaded by the Raspberry pi powering the E-ink display.

## Features

### Basic

 - [X] Download highlights & additional data from [here](https://read.amazon.com/kp/notebook)
 - [X] Randomly select highlights
 - [X] Load additional data
 - [ ] Display data by creating images using PIL
 - [ ] Raspberry pi auto loads highlights on boot up
 - [ ] Highlight list is updated weekly

### Stretch
- [ ] multiple, configurable output layouts
- [ ] Reduce highlight pool

## Output Example
<img width="796" alt="image" src="https://user-images.githubusercontent.com/41706121/174710797-2c6eeae1-f2c3-40c1-9ea1-276ed9c5c11d.png">

## How to Use
1. Create a "credentials.txt" in the root directory. First line is your amazon username, second line is your amazon password.
2. Setup a cron-job to run `download_highglights.py` on a weekly (or whatever you want) basis.
3. Setup another cron-job to run `main.py` every 10 minutes (or whatever you want.)
4. Connect the device to an e-paper display & configure it.

