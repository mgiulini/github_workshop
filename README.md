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

  substitute this dummy address with the one you just copied.
