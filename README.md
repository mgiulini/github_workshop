# github_workshop

## Exercise 1. Creating repositories, managing collaborators, and cloning

### Creating a repository
One group member has to create a repository in their own github account

- Go to [github.com/YOUR_USERNAME]
- select *Repositories*
- click *New* and choose a name for your repository (e.g. "github-tutorial", "my-first-github"). Avoid spaces in repository names
- leave the repository as public
- tick the Add a README file box: this will authomatically add an empty README file to your new project. 

**Tip**: for projects involving sensible data, it is advised to create a repository in *private* mode. It is anyway always possible to change the visibility of the repository later, for example when you are about to submit a research paper and you want to make the data available.

### Managing collaborators

Now your repository should have been created. In this situation the repository is public, and therefore visible to everyone, but the person who created it is the only allowed contributor. Let's see how we can easily add contributors:
- go to the main page of the repository
- click on *Settings->Collaborators*
- click on the Add people button
- you can now use the other members' github usernames to grant them full access to the repository.

### Cloning

The other group members should have received an e-mail with the details about the shared repository.

It's now time that everyone of you has a copy of the online repository on your laptop.

- open the terminal on your laptop
- search the directory where you want to have your clone of the project (Desktop is also fine)
- Back to the browser: go to the main page of the repository
- click on the green **Code** button on the top-right side
- copy the link available under the HTTPS menu

- Back to the terminal, write down the following command:
  ```bash
  git clone https://github.com/YOUR_USERNAME/...
  ```

  substitute this dummy address with the one you just copied. You will be asked for your credentials: once you provide them, the download will start and you will have a local copy of the repository on your laptop!

## Exercise 2. Add, Commit, Push

Now that we have a shared repository, let's add something to it.

[Here](example/order_models.py) you will find a very simple python script that reads [some data](example/capri_ss.csv) about possible models of a biomolecular complex, and ranks them according to a scoring function, built by combining three different features of the data. The lower the score, the better the model.

The following instructions should be only executed by one group member. The others can have a look.

1. Download the script and the data files, and move them to the repository directory.
2. From the terminal, navigate to the repository directory.
3. Try the script to see it it works properly on your computer.
```bash
python order_models.py
```

4. Once you're sure the script works, check for the changes within the repository
```bash
  git status
```
  This command will tell you the current state of the working directory. You should see something similar to this ![image](figures/status.png)

5. add the script to the staging area:
```bash
  git add random_diff.py
```
..and don't forget the data!
```bash
  git add capri_ss.csv
```
  and check again for differences
```bash
  git status
```
  You added something to the staging area!
![image](figures/staged.png)
  Nothing is definitive yet, you can in principle still apply local modifications to the file and re-add it.
  
6. You are now convinced of the changes you made, time to commit them.
```bash
  git commit -m "added python script and data"
```
   The commit just created a snapshot of the repository at this point in time. It is important to write down meaningful commit messages, so that other collaborators (and future versions of yourself) can have an idea of what you've done.

7. The commit you made is now available only on your local clone. It's time to push your changes to the remote.
```bash
  git push
```

The other group members can now update their own clones with the new content available on the remote
```bash
  git pull
```

## Exercise 3. Working in parallel. Issues, Branches, Pull Requests

You or one of your colleagues decide that the project needs some changes. In our research context, let's assume that this means refining and improving our approach according to the following features.

1. Our new score should contain the 'bsa' (buried surface area) value, that should be weighted with a weight equal to 0.01 in our score;
2. unfortunately one model (**model_108**) has to be discarded, together with all the associated data (row), as we discovered that it was obtained with a wrong procedure;
3. our repository should contain a short piece of documentation to explain our approach to the problem.




