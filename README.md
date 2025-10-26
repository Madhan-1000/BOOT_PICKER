# HTML to CSS Converter

Well any one wondering why this project is made??

Recently I have been learning about Bootstrap and I thought what if some one wants to rewrite code of this it has to be a hassle.

That is why I created this project.

An Application that takes HTML Code as input and gives CSS Code of respective classes.

Right Now there is only css that needs to be handled and soon JS is coming as form of animation.

## Deployed On Render

https://boot-picker-hfbk.onrender.com

## Overview

This project is a web application designed to simplify web development by converting HTML code into corresponding CSS styles. You input HTML code, and the application generates the CSS needed to style the respective classes, making it easier to redesign websites without starting from scratch. The tool aims to save time and reduce the hassle of manually writing CSS for Bootstrap-based or other HTML structures.

![Project Screenshot](static/images/logo.png)

## Features

- **HTML to CSS Conversion**: Input HTML code, and the application outputs CSS styles for the classes used.
- **User-Friendly Interface**: Simple and intuitive design for developers to quickly generate CSS.
- **Future Enhancements**: Plans to include JavaScript support for animations to further enhance website redesign capabilities.

## File Structure

Here’s the structure of the project:
```BOOT_PICKER```
```
├── app.py 
├── LICENSE
├── requirements.txt
├── static
│   ├── css
│   ├── data
│   │   └── data.json
│   ├── images
│   │   └── logo.png
│   └── js
└── templates
├── About_us.html
├── Help.html
└── index.html
```

```Cloning:```

```
git clone http://github.com/Madhan-1000/BOOT_PICKER
cd BOOT_PICKER
```

```Virtual Environment & Running:```

```
python -m venv venv
#On MacOS
source venv/bin/activate  
# On Windows: 
venv\Scripts\activate

```

```Requiremnts Installation:```

```
pip install -r requirements.txt
```
```Run Application```
```
python app.py
```

**One-Shot Command**:

```
git clone http://github.com/Madhan-1000/BOOT_PICKER
cd BOOT_PICKER
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
