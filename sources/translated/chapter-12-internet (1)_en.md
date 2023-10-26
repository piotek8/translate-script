\pagebreak

# Internet

Here we will discuss various issues related to the network, the Internet, and everything else. Despite the fact that as a junior-python wannabe we are most concerned about Python itself and programming, we must remember that the code we write and then run does not operate in a vacuum. 

All our web apps, programs, etc. are run in a specific environment. This environment affects the execution of our programs, how they operate. Additionally, we often have to interact with it in some way, often reciprocally. What does this mean? Well, aside from our Python, we should also know the whole environment where this hustle and bustle takes place, since otherwise, we may sometimes trip ourselves up. Moreover, knowledge of the environment and related matters, which we use either directly or indirectly, often without realizing it, i.e. simply other components of the `System` that we design, create or maintain, are an integral part of it as well as something that influencesand our work and our code.

By System, I mean some kind of arrangement, a set of elements. In IT, it's usually, for example, our web app, servers where it is run, client, etc.

So, let's talk about this whole system and environment.

## Request Path

Most web applications operate on a client-server model. The client makes requests to the server, the server returns a response.

But how does it happen that we are able to send this request. What happens at the moment when you type `grski.pl` into the browser's address bar and then you see my blog?

Well, the matter looks like this.