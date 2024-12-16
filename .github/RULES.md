# Branches
## Main branche
Hold the production ready code after a **pull request** was created from the develop branche.

## Develop branche
Holds the code in development. This code is agreed on by the team and originated from the feature branches.

## Feature branche
When we develop a new feature, to be sure no problems will arise, instead of coding directly into the develop branche we create a feature branche for each feature. the feature branches are created from the develop branch each time.

**Naming the branch:**
`feature/{Task_ID}-{branche name}`

## Proof Of Concept (POC) branche
When there is an idea that we need the team to look at and test it we create a POC branch. Similarly to the feature branche, the POC branch is created from the develop branche.

**Naming the branch:**
`poc/{Task_ID}-{branche name}`

## Fix branche
If a problem arises in the develop branch code or the main branch code we created a Fix branch from any of them. Here we implemet the fixes we will introduce.

**Naming the branch:**
`fix/{Task_ID}-{branche name}`
