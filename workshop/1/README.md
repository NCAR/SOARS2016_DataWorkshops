# WORKSHOP 1

> Start by doing what's necessary; then do what's possible; and suddenly you are doing the impossible.  ~ Francis of Assisi (1182 - 1226)

## Tools
In this workshop we're going to learn a little about the tools and language we'll repeatedly access through the summer.  First on to the tool chain we're going to work with :

| Tool | Purpose |
|------|---------|
|Python|This is the language we'll be using this summer.  Let's make sure it is installed and ready to use.  If you went through the [installation](../README.md) tutorial, you should be good to go. |
|PyCharm|This is our editor (one of many you could use).  It is full functioning and pretty friendly once you get the hang of its functions.  PyCharm is excellent for writing longer, more complex code in a project-like environment.  Let's see that everything is OK with the [installation of PyCharm](../README.md). |
|Github|[Github](https://github.com) is an excellent place to share, find and contribute to open source projects of all kinds.  There are millions of repositories representing everything from scientific projects to programming langages, web servers and websites.  You can get lost on there! |
|Jupyter Notebooks|We'll affectionately use NB as a shorthand for Jupyter Notebooks, but this tool is the backbone of data exploration in Python these days.  With support for so many interesting things, you'll soon find out that you can do a lot of great things and share them with others when you're done. Support for NB is OK in PyCharm, but we'll play mostly with it directly in the browser on the server that we'll invoke from within PyCharm.|

## The Python Language
Python is the language of choice these days for many of the data science and analytics tasks we're faced with on a day-to-day basis.  There is a basic assumption that you have had _some_ exposure to at least _one_ programming language, but if you need to brush up on some basic concepts, check out the [resources page](../resources.md) for more places to learn about Python.

To get started, let's review the [Python Primer](primer_python.md) that will go over the **very basics** of the language and get your feet we in what it is all about and what it can do.

## Github in 10 minutes or less
[Github](https://www.github.com) is a system / web application / platform that provides a beautiful way to store, view, manage, share and revise code.  While the primary content on Github is _running_ software, whether that be in C, Java, HTML, Python or the many hundreds of other languages in popular use today, it can also be a place for traditional text files (data, papers) and other binary data (Word/Excel documents, images, etc.)  Github's strength is in the ability for it to facilitate software collaboration, and today it is the premier place on the web for large scale open-source, collaborative software projects.  Though open and public projects are Github's forte, it provides the ability for you to host private projects and allows you to make the decision later whether it is appropriate to make such projects public or not.

### Revision Control in 60 seconds
Github is built on top of what is called **git**, which is a __revision control system__.  The core concept behind such systems is that they manage your text-based code files and allow you to keep track of the changes (revisions) to those files.  In a system like **git** you can invite others to work on your code as well, which can allow more than one person to make contributions to the code.  What is even more useful is that such changes can be tracked across a project so that those contributions and changes can be seen, reviewed, modified and otherwise managed.  Thus, when someone (even you) makes a change to a file (or files) and makes those changes known to the revision control system, others with access to those files can not only see those changes, but integrate them into their own.

Git provides a great deal of functionality which might appear to be complex and overwhelming.  Most of the functionality you will need in the basic daily use case is very narrow, so don't be discouraged by the depth and complexity of git's documentation.

### What's Git all about?
In revision control systems you code is typically stored in a **repository** and that repository most often lives and is managed on a remote server.  This is done for a variety of reasons, one if which is to provide others access to your code.  Git has the advantage of such code and its revisions being controlled locally and only when you're ready can those changes be put onto the remote server.  The relationship between Git and Github is that Github provides a nice visual shell over Git and also serves as the remote git server, so you don't have to think about it when you want to share your code with others (or have a remote copy of it).

You will always need to install git on your local system, and don't ever _have to have_ a remote server, but if that is the case, the code in such a local project will never be seen by, or syncronized with (backed up on) a remote server, thus making it difficult to (though not technically impossible) share with others in the general case.

### Projects <=> Repositorities
In git your code lives in a repository.  This is simply the location / directory for your files and it lives (initially) local to your file system.  You can create a repository anywhere on your file system, but it is often a good practice to keep git repositories in a common location when it makes sense to do so.  Furthermore  there is no limit to the number of repositories or the number of files under the control of a repository.

You can consider a repository as a project containing a single focus of interest.  For example, you might think if your repository as containing a single complete software application you're building.  Similarly, you might think of it as a place for all the files of a single course over a semester, or a single topic of interest.  Your concept of "project" isn't really restricted, though there are some best practices.

 In Github, as in git, the anchor of a project is the repository.



## A Primer on Text-based Data Files

For starters, many of the files you'll be working with through the summer (and beyond) are in some text format or another.  The most popular (generally) being CSV or TSV (comma separated, tab separated, respectively).  Netcdf is very common binary format used in the Geosciences, and we'll touch in on them if we have time.  Python makes doing basic operations on text files very straightforward, hence its use as a language of choice text processing language.

We'll get started with a review and shallow dive [into processing text files in Python](primer_files.md).




