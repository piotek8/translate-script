\pagebreak

# Internet

Here, we will discuss various issues related to the network, the Internet, and everything else. Despite the fact that as a junior-python wannabe, we are most concerned about Python itself and programming, it is important to remember that the code we write and then run does not operate in a vacuum.

All our web apps, programs, etc. are run in a specific environment. This environment interacts with the way our programs are executed, how they function. Additionally, we often have to interact with it in some way, often mutually. What does this mean? Well, in addition to knowing our Python, we also need to understand the full scope of where it operates and so forth, otherwise, we might occasionally shoot ourselves in the foot. Knowing about the environment and related things, which we directly or indirectly use, often unknowingly, namely the rest of the `System` that we design, create, or maintain, is an integral part of it and something that influences it.and our work and our code.

By System I mean some arrangement, a set of elements. In IT, it is usually, for example, our web app, servers where it is run, the client, etc.

So let's talk about this entire system and environment.

## Request Path

Most web applications operate in a client-server model. The client makes queries (requests) to the server, the server returns a response.

However, how does it happen that we are able to send this request. What happens at the moment when you type `grski.pl` into the browser bar and then you see my blog?

Well, the matter looks as follows.