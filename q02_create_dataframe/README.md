# Create Data Frame

This assignment comprises of taking the data and converting it to dataframe. About Dataframe you will be learning about in the coming sections.

## Write a function `q02_create_dataframe` that :
- Previous function to load the data
- Use `re` library to remove non alphanumeric characters. Note - use `'[^a-zA-Z]'` this pattern search to pass the testcases.
    You can also refer to `re` documentation to explore more.
- Use `Counter` function to count the frequency of the character (return type of this is dictionary) and convert them to dataframe.
- Use  `pd.DataFrame` to convert to dataframe with column name words and count.

### Parameters :
| Parameter | dtype | argument type | default value | description |
| --- | --- | --- | --- | --- |
| path | string | compulsory |  | path of the csv file location |

### Returns:
| Return | dtype | description |
| --- | --- | --- |
| variable | pandas.Dataframe | Dataframe with above operations inculcated |