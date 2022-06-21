# Kindle-Highlights-Display
This is the software repository for my highlights project. This repo has two parts. The first being a webcrawler that downloads and saves your highlgihts from the amazon website. The second being the software behind the physical display. It chooses a random highlight, uses an API to download additional information (such as book name, author, cover art, etc.) And displays it into a PIL image to be loaded by the Raspberry pi powering the E-ink display.

## Features

 - [X] Download highlights & additional data from [here](https://read.amazon.com/kp/notebook)
 - [X] Randomly select highlights
 - [X] Load additional data
 - [ ] Display data by creating images using PIL
 - [ ] Raspberry pi auto loads highlights on boot up

## Output Example
<img width="796" alt="image" src="https://user-images.githubusercontent.com/41706121/174710797-2c6eeae1-f2c3-40c1-9ea1-276ed9c5c11d.png">

