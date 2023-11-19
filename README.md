
# Part One: AirBnB Console
## ✈️ Description of AirBnB Console Project

## 0x00. AirBnB clone - The console

`Group project`
`Python`
`OOP`

- By: Guillaume
- Weight: 5
- Project to be done in teams of 2 people (your team:Tekoh Palma ACHU)
 Project will start Nov 6, 2023 4:00 AM, must end by Nov 13, 2023 4:00 AM
- Checker will be released at Nov 11, 2023 10:00 AM
 Manual QA review must be done (request it when you are done with the project)
- An auto review will be launched at the deadline

### Concepts

For this project, we expect you to look at these concepts:

- [Python packages](https://intranet.alxswe.com/concepts/66)
- [AirBnB clone](https://intranet.alxswe.com/concepts/66)

![AirBnB_image](./img/img.png)

### Background Context

#### Welcome to the AirBnB clone project

Before starting, please read the AirBnB concept page.

First step: Write a command interpreter to manage your AirBnB objects.
This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (`User`, `State`, `City`, `Place…`) that inherit from `BaseModel`
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

### What’s a command interpreter?

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## Resources

### Read or watch

- [cmd module](https://intranet.alxswe.com/rltoken/8ecCwE6veBmm3Nppw4hz5A)
- [cmd module in depth](https://intranet.alxswe.com/rltoken/uEy4RftSdKypoig9NFTvCg)
- [packages concept page](https://intranet.alxswe.com/concepts/66)
- [uuid module](https://intranet.alxswe.com/rltoken/KfL9TqwdI69W6ttG6gTPPQ)
- [datetime](https://intranet.alxswe.com/rltoken/1d8I3jSKgnYAtA1IZfEDpA)
- [unittest module](https://intranet.alxswe.com/rltoken/IlFiMB8UmqBG2CxA0AD3jA)
- [args/kwargs](https://intranet.alxswe.com/rltoken/C_a0EKbtvKdMcwIAuSIZng)
- [Python test cheatsheet](https://intranet.alxswe.com/rltoken/tgNVrKKzlWgS4dfl3mQklw)
- [cmd module wiki page](https://intranet.alxswe.com/rltoken/EvcaH9uTLlauxuw03WnkOQ)
- [python unittest](https://intranet.alxswe.com/rltoken/begh14KQA-3ov29KvD_HvA)

## Learning Objectives

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General

- How to create a Python package
- How to create a command interpreter in Python using the cmd module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- How to manage datetime
- What is an UUID
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

### Copyright - Plagiarism

- You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
- You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
- You are not allowed to publish any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements

### Python Scripts

- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- Python Unit Tests
- Allowed editors: vi, vim, emacs
- All your files should end with a new line
- All your test files should be inside a folder tests
- You have to use the unittest module
- All your test files should be python files (extension: .py)
- All your test files and folders should start by test_
- Your file organization in the tests folder should be the same as your project
- e.g., For models/base_model.py, unit tests must be in: tests/test_models/test_base_model.py
- e.g., For models/user.py, unit tests must be in: tests/test_models/test_user.py
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: python3 -m unittest tests/test_models/test_base_model.py
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

### GitHub

There should be one project repository per group. If you clone/fork/whatever a project repository with the same name before the second deadline, you risk a 0% score.

## More Info

### Execution

Your shell should work like this in interactive mode:

```$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)

```$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)


Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

# Architecture of the System

![AirBnB Architecture](./img/architecture_Airbnb.png)


## How to use the Console

#Part Two:AirBnB Web Static

# 0x01. AirBnB clone - Web static
`HTML`
`CSS`
`Front-end`
 - 🤵By: Guillaume
 - 💠 Weight: 1
 - 📆 Project will start Nov 16, 2023 4:00 AM, must end by Nov 21, 2023 4:00 AM
- ✅ Manual QA review must be done (request it when you are done with the project)
### Concepts
For this project, we expect you to look at these concepts:

- [HTML/CSS](https://intranet.alxswe.com/concepts/2)
- [The trinity of front-end quality](https://intranet.alxswe.com/concepts/4)


## Background Context
### Web static, what?
Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:

- Create simple HTML static pages
- Style guide
- Fake contents
- No Javascript
- No data loaded from anything
During this project, you will learn how to manipulate HTML and CSS languages. HTML is the structure of your page, it should be the first thing to write. CSS is the styling of your page, the design. I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.

Before starting, please fork or clone the repository AirBnB_clone from your partner if you were not the owner of the previous project.

## Resources
### Read or watch:

- [Learn to Code HTML & CSS (until “Creating Lists” included)](https://intranet.alxswe.com/rltoken/T9KyiA6_Tm3Ny6oTn08S-A)
- [Inline Styles in HTML](https://intranet.alxswe.com/rltoken/7NdYbImFNofpB_FXXn3otg)
- [Specifics on CSS Specificity](https://intranet.alxswe.com/rltoken/z_OTPFCjmhXJJi7KJqBCbQ)
- [CSS SpeciFishity](https://intranet.alxswe.com/rltoken/orI812cozq-yd2769VdM_w)
- [Introduction to HTML](https://intranet.alxswe.com/rltoken/okP4V3RxFXHkEcQo19AnuQ)
- [CSS](https://intranet.alxswe.com/rltoken/Ir8Ka59FO6Z_vJQ-gkSG_w)
- [MDN](https://intranet.alxswe.com/rltoken/BpSXtcWOGH0UT4XLCoQyJg)
- [center boxes](https://intranet.alxswe.com/rltoken/Tlje4XYwyZbUfHkQWGi1WQ)
## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

### General
- What is HTML
- How to create an HTML page
- What is a markup language
- What is the DOM
- What is an element / tag
- What is an attribute
- How does the browser load a webpage
- What is CSS
- How to add style to an element
- What is a class
- What is a selector
- How to compute CSS Specificity Value
- What are Box properties in CSS
### Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should be W3C compliant and validate with [`W3C-Validator`](https://intranet.alxswe.com/rltoken/RGLQtJVf7Ga3mU8NX9zADQ)
- All your CSS files should be in `styles` folder
- All your images should be in `images` folder
- You are not allowed to use `!important` and `id` (`#`... in the CSS file)
- You are not allowed to use tags `img`, `embed` and `iframe`
- You are not allowed to use Javascript
- Current screenshots have been done on `Chrome 56` or more.
- No cross browsers
- You have to follow all requirements but some `margin/padding` are missing - you should try to fit as much as you can to screenshots
## More Info
![web_static Architecture](/images/web_static_architecture.png)
## Description of team 💻

Due to difficulty in finding a serious Partner the development team was made up of Tekoh Palma Achu
who Build the app Solo 🥇
