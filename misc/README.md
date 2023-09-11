# Get Gitlab schema 

```shell

devbox shell
npm install get-graphql-schema

./node_modules/.bin/get-graphql-schema --header "Authorization=Bearer GITLAB_PAT" https://gitlab.com/api/graphql > ../schema/gitlab_api.schema
```
