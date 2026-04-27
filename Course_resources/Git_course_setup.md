# Set up BI621 with Git

## Set up Git/GitHub
Be sure you have a [GitHub](https://github.com/) account and be sure you have [git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) installed on your computer. See our [Canvas site](https://canvas.uoregon.edu/) for detailed videos on these topics.

After creating your GitHub account, optionally request an Education account [here](https://education.github.com/discount_requests/new).

Test your installation by issuing the command `git` on the terminal. You should see something like the following:
```
usage: git [--version] [--help] [-C <path>] [-c name=value]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

These are common Git commands used in various situations:
```
Here are some [Git and GitHub learning resources](https://help.github.com/articles/git-and-github-learning-resources/) to help.

Be sure you have provided your GitHub name to Leslie so you can be added to the 2026_Bi621 repository. Look for the invitation link in the email address you provided GitHub.

## Setup 2026_Bi621 on your computer

Before performing the steps in this section, be sure you have:
- Git installed on your computer.
- A GitHub account.
- (optional) Accquired an Education discount for unlimited free, private repositories.
- Accepted your invitation to collaborate on the `2026_Bi621` repository.

You're now ready to clone the repository onto your machine. Note we're setting up this cloned repository so that you do not accidentally push to the shared course repo. **You do not need to do this if you're cloning a course assignment repo.**

1. Create the appropriate file structure and clone the repository by issuing the following commands (if you're new to using the command line, *note!* the `$` is not typed, it's merely indicating the prompt):
	```bash
	$ cd
	$ mkdir bioinfo
	$ cd bioinfo
	$ mkdir Bi621
	$ cd Bi621
	$ git clone https://github.com/Leslie-C/2026_Bi621
	```
	Note that this should fail if you type in your GitHub username/password. GitHub is requiring users to use tokens now. Follow the directions found [here](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) or watch the [video](https://uoregon.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=4fbebf2b-c923-4c05-b9aa-ae9301872f24) on our Canvas site.

	Once you have set up your token, run
	```bash
	$ git clone https://github.com/Leslie-C/2026_Bi621
	```

	again, this time entering your username and the token you just created.

	Change to the newly cloned repository:
	```bash
	$ cd 2026_Bi621
	```
	
	In the future, you can stop here if you're cloning an assignment repo.
	
2. By default, the remote called `origin` is set to the location you cloned the repository from. You should see the following:
	```bash
	$ git remote -v
		origin	https://github.com/Leslie-C/2026_Bi621 (fetch)
		origin	https://github.com/Leslie-C/2026_Bi621 (push)
	```
	We want to change the origin to be YOUR repository and the class repo to be the upstream repo (pulling from only). To do this:
	```bash
	$ git remote rename origin upstream
	```
	And you should see:
	```bash
	$ git remote -v
		upstream	https://github.com/Leslie-C/2026_Bi621 (fetch)
		upstream	https://github.com/Leslie-C/2026_Bi621 (push)
	```
3. On your GitHub account, click the `New Repository` button.
4. Enter a repository name. I suggest `2026_Bi621` or similar. Add an optional description, and make the repository `Private`. Do NOT initialize with a `README`. Create the repository.
5. On your own computer, issue the following command, but with your GitHub username in place of \<username\>. If you called your repository something other than `2026_Bi621`, be sure to change that as well.
	```bash
	git remote add origin https://github.com/<username>/2026_Bi621
	```
	Now you should see:
	```bash
	$ git remote -v
		upstream	https://github.com/Leslie-C/2026_Bi621 (fetch)
		upstream	https://github.com/Leslie-C/2026_Bi621 (push)
		origin	https://github.com/<username>/2026_Bi621 (fetch)
		origin	https://github.com/<username>/2026_Bi621 (push)
	```
6. Test your setup:
	```bash
	$ git push -u origin main
	```
	You should see something like the following:
	```bash
	Counting objects: 4, done.
	Delta compression using up to 4 threads.
	Compressing objects: 100% (4/4), done.
	Writing objects: 100% (4/4), 1.73 KiB | 0 bytes/s, done.
	Total 4 (delta 1), reused 0 (delta 0)
	remote: Resolving deltas: 100% (1/1), completed with 1 local object.
	To https://github.com/<username>/2026_Bi621
	   9231e8d..47fba44  main -> main
	```
7. From now on, you can just issue `git push` without the arguments to push your changes to your online (GitHub) repository. Try it out!
	```bash
	$ git push
		Everything up-to-date
	```
8. As new materials are added to the course repository, be sure to
	```bash
	$ git pull upstream main
	```
	to keep things up-to-date.
