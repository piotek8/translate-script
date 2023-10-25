\pagebreak

# Setting up the environment

Let's finally move on to something concrete – let's get our hands a little dirty because so far I've only been talking and talking. We will start by setting up the environment/installing Python and something to edit text. Just a moment, what? There are two options - a simple text editor or an IDE. What will we choose?

## What to write code in at the beginning?
In what to write code at the beginning? IDE/Text editor? PyCharm? Sublime? VS Code?

When I think about my first days of learning to program, one of the many things that kept getting mixed up in my head and brought a lot of trouble in resolving them was the choice of the environment where I would be writing my first programs.

However, it's not surprising - now practically for every language there are at least several free IDEs, plus there are paid ones, we also have text editors and so on. It's easy to get lost. At least that's what I did and instead of learning programming for a few days, I sat and pondered the choice.Environment.

### IDE? Text editor?

So how is it? IDE or text editor? And what is an IDE in the first place? Find out for yourself — as an IT specialist, your primary task is information processing. Search the internet for the meaning of this abbreviation, look up the differences between an IDE and a text editor.

I won't serve it to you on a platter, because the ability to find information is a key trait that makes a good IT specialist/programmer, and it needs to be practiced from the beginning, and I will try to develop this in you throughout the pages of this book.

So, what to choose? The answer may surprise you — it's: it doesn't matter much. Let me explain.

Whether you choose CodeBlocks, VisualStudio or Atom, in my opinion, doesn't matter much, because these are just tools. Tools in the hands of the programmer, and it depends on them how well these tools will be used. Just like with languages.

Even the best IDE will not help you if you do not know how to use it. On the other handIndeed, if you master the operation of seemingly prehistoric, by today's standards, programs like Vim or Emacs, you can perform miracles.

Therefore, I recommend not to pay too much attention to which environment one chooses, as practically any can be adapted and made to work excellently in.

Despite this, however, one can perhaps outline one of the paths that are worth taking and which I think are quite sensible. What is this path?

### Basics

Regardless of whether we use an IDE or any text editor, it is good to know how it all works from the inside out, which I have repeated several times and will repeat many more times.

So that it is not the case that someone without their IDE is unable to compile a piece of C++ code or launch a Python script from the console. Such basic things should be learned because they allow a better understanding of how programs are created and how it all works, these pieces of information are sometimes simply essential.

In addition to this, onAt the beginning, the code suggestion feature should be turned off. By typing out the names of instructions, methods or classes, we will learn them faster. At least that's how it was for me. By using auto-complete, it was often enough for me to type two or three letters, hit tab, and voila – done.

The problem arose when I ran out of auto-complete, because for example, I had to write something quickly in a plain text editor/use someone else's computer or, horror of horrors, go for a job interview, where I had to write code on a board with a marker. I won't tell you how stupid I looked a few times because of that.

Suddenly, everything flew out of my head and I forgot half the commands that I supposedly knew so well. So right from the start, I gave up on automatic completion in favor of manual typing.

So in the beginning, it's better to forget about syntax suggestions, especially if you're planning on going for a job interview in a while. Although I doubt it, since you're reading this book.

Later, when I had already memorized a sufficient amount...Here's the translation: 

Organically, keywords, instructions, I went back to it again and again. However, to start with, I would not recommend auto-completion.

### How it looked like for me

What environment did I choose?

Frankly, I tried many different ones, following roughly this path while learning Python:

At first, I was writing in the browser, doing a course on one of the interactive programming academies - I didn't need to download any software, but later, when I wanted to start writing something of my own on the disk, I looked around the internet and found various threads where PyCharm and a few other popular IDEs were usually recommended. So, I downloaded them. But only for a short period.

They were too overwhelming for me - a multitude of options, complexity. Moreover, my old laptop struggled with the hardware requirements of such IDEs. Working with them was essentially barely possible.

So I switched to SublimeText, where I stayed a little longer, slowly getting accustomed to the console and the fact that I had to do some things myself. After a certain tI started missing something in Sublime, so I started searching again — I came across Vim and used it for a while.

Fantastic tool. Swiss Army knife — you can do anything with it. It can be a lightweight text editor or a full-fledged IDE, with the right amount of plugins. I liked its configurability, the magic you can do with it.

At the beginning it was hard, but then I got a little used to it. Nevertheless, I don't really recommend Vim as a first text editor, it is a bit different to use than standard programs.

I changed from Vim to SublimeText for short and simple scripts, and I write all the rest of the applications in PyCharm. It offers too many useful options not to use it, and secondly, it has become a standard in our industry, and there are really few companies that do not use it.

I started missing something in Sublime, so… Back to Vim + PyCharm. And this is my personal history.The stack has been set up for several years now.

For the needs of this book, SublimeText will be fully sufficient for you, then we may possibly switch to PyCharm. Let's move on to the installation since we already know what we will need.


## Windows?! Linux?! MacOX?! What to choose?

Doesn't matter.

Either here or somewhere else, enthusiasts of one system or another will appear soon and they will desperately try to convince you that the system chosen by a given person is the best and only suitable for use/programming/anything.

Don't bother with them. The system is just a tool and it depends on you whether you use it efficiently or not. Unless you care about languages that in some way limit the freedom of choice because, for example, if you want to write applications for iOS in Swift, you probably won't be using Windows, similarly writing software in pure C#, you probably won't be using macOS. Simple thing.

However, this does not apply to us. We are simple Python users. And it's pretty cool for us.It runs everywhere.

However, it's good to have at least basic understanding when it comes to Linux. Why? Practically every server where we host our applications on the network is based on Linux. Sooner or later you'll come across it, and if you are somewhat familiar with it before that happens, it won't be a painful clash with reality where you hit your head against the wall, but rather a beer meeting with a good buddy you haven't seen for a long time. That's one. Two, generally, certain things on Linux you have readily available, where on Windows you have to struggle with some things yourself, install, etc. Does this mean you have to install a new system in order to get to know Linux; you can't live otherwise?

Absolutely not. All you need is a virtual machine with any distribution. I personally recommend Ubuntu, even though I'm not a fan of Canonical, and the second option, Manjaro. Both are Linux, but with some differences. Personally, when I use Linux, it's Manjaro. At least on the desktop. Because on...Manjaro servers are rather out of the question.

Virtual machine, what, how, where? Look through the table of contents, you should find the answer in this book, although it might be a bit further on.

Moreover, there has been another one available recently - WSL. Windows Subsystem for Linux. It's like a Microsoft toy, that allows you to have Linux integrated with your Windows. Linux in Windows from Microsoft. Boom. The advantages are easy installation, easier integration etc. In general, I recommend it.

To summarize briefly, both Linux and Windows have their advantages and disadvantages, they are just tools. I, personally, however, am finally using Linux as a host. If you are using Linux, that's cool, if not, be sure to install WSL.
## Installation on Windows
Usually, in Python books, we find a step-by-step description of Python installation, helpful screenshots, and so on. Well, not here. We will install the things we need in a somewhat untypical, for Windows, way. And then...by the power of the console. No, I haven't lost my mind.

I don't know if you're aware, but Linux users usually install programs in a slightly different way than Windows users. 

Well, every popular Linux distribution contains what is called a package manager. You can think of it as a 'program' that manages all officially supported and available programs for a given distribution. Clear, right?

Thanks to these so-called package managers, Linux users can do something cool - most programs on Linux can be installed with a single command, the same goes for their update, system update, or deletion of 'programs'. Things are a bit different on Windows. For me, the way Linux manages packages is more convenient, and I'm sure many people will agree with me at this point.

Unfortunately, by default, Windows does not have a sensible package manager, but I deliberately used the term 'by default' here. There is a very cool tool called chocolatey, which isand allows us to achieve such functionality as pacman or apt provide.

In short, thanks to it, installing a large part of the programs is reduced to:

choco install program_name

And that's it. Convenient, huh? That's why we will use this package manager to install what we need.

We install Choco
Detailed instructions can be found on the [chocolatey page (https://chocolatey.org/install) ](https://chocolatey.org/install) and that's where you need to go to find out how to install choco.



### Installing the things we need using choco
Chocolatey installed? Just one command now separates us from the finish.

```bash
choco install python sublimetext3 -y
```

And that's it. What if we want to update all/selected programs?

Again, nothing simpler:

```bash
choco upgrade all
```

or

```bash
choco upgrade program_name
```

I guess I don't need to translate. The list of packages available for installation in this way can be found tKeep it secret. Most popular programs are there.

If we don't feel like clicking 'y' for each upgrade question, simply add `-y` at the end of the command, similarly to the example with installing SublimeText.

Now we just open SublimeText, create any directory anywhere and in SublimeText we click File → Open Folder, selecting the folder we created earlier, which will serve as our main folder for the files from this book.

## Installation on Linux/macOS
As for the instructions for Linux or macOS and its users. Well, there's none for you.

But why? What kind of discrimination is this? Well, you probably already have Python installed, just check which version. How?

```
python --version
```

(two dashes) in the console and you're ready, or, depending on the distribution, it may be

```
python3 –-version
```

It depends on which distribution you are using and which version of Python it uses as the default.

Ideally, it should be Python version >= 3.7.0. If it's not, upgrade it.

How to do it? Let's be honest, if you're using Linux, you probably don't need to ask me about this. Same goes for installing SublimeText. And if you really have no idea about it… Remember what I said about the most essential skill of a computer scientist - processing information. Start searching, then.

As for the Mac? Use the `brew` tool. That's it.

And as I mentioned, it doesn't have to be SublimeText - you can use your favorite editor. It doesn't matter. But please, don't use Windows' Notepad for this. Every time you do that, a kitten somewhere in the world dies. Don't do it.

## Let's move on to programming! Finally!

Well, not quite yet. Now we have to navigate to the main code directory for this book, which we recently created, using the console, of course.

To do this, you need to open the console again. This time, you won't need administrator mode, so open it as a normal user, whether on Linux or Windows.

And what now? It's time to get familiar with basic commands, wh...These may come in handy for you. Mainly, there are four basics that I will discuss, but there are of course many more, and some of them, which may be needed in your daily work, we will discuss later.

I simply don't want to overload you with information that you will not need yet, and simply add things to the list of issues that you need to comprehend.

## Four Horsemen of the Console

1. `dir` (Windows) or `ls` (Linux). This is a command that lists the contents of the directory we are currently in the console. How do we know where we are? Simple - our working directory (CWD - current working directory) is displayed on the left side of our terminal cursor or by entering pwd on Linux/iOS. Windows users google. They wanted Microsoft's systems. Now they have it. What does it give us to be in a directory?  
Well, our commands will be executed relative to this path. So if we enter `python file.py` then if we are in the folder let's assume `C:\Users\O
laf` will make Python look for this file, the file.py, in this folder.
1. `mkdir` - common for both systems, creates a directory with the given name e.g. mkdir folder will create a folder named folder in the current working directory. Makes sense.
1. `del` (Windows) and `rm` (Linux) - these commands are used to delete files. If we want to delete a folder, we can use rd on Windows or rm -rf on Linux. Example of use: rm -rf file.txt.
1. `cd` – common for both systems. Cd, which stands for change directory. It changes the current working directory to the specified one. An example of use - cd .. - this command will take us to the parent directory in the file structure. So if we are in `C:\Users\Olaf\Test\`, using cd .. will take us to `C:\Users\Olaf\`.

Useful information: clicking TAB causes the console to auto-complete the names of directories or files;

On Linux (usually) the symbol ~ denotes the user's home directory, so if you want to go there, you don't have to give the full path. Just usewrite cd ~ and that's it.

One more note, not all Linux systems have the current working directory imported into the PATH, so sometimes there may be a need to specify the file location in the current CWD as ./file.txt instead of file.txt, depending on the distro. This can easily be fixed by adding the CWD to the PATH. The same may be true with Python itself. Remember to add it to PATH during installation. Or, if not during installation, you can add it manually later.

How? Google it, Linux user. You wanted to install Linux systems, now you have it. And struggle, struggle, as you wanted, whether you're a he or she!

We already know how to navigate, but we will come back to the console. How to run our source code?

Simple.

```
python file_name.py
```

Notice, if you are on Linux and you had Python 2 installed before, you might need to use the python3 command to run it, but you probably know that.

And to run the Python interpreter, just type:

```python
python
```

And that's it. This will launch the interpreter. RThe difference between an interpreter and running from a file is that in the interpreter, we enter commands and Python interprets them on the fly. In the case of a file, we have a less interactive approach. Play around and see for yourself.

Environment sorted, navigating the console as well. We finally get to work!

\pagebreak