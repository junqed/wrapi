### Requirements:   
* Python 3.7+

### Example of usage:

```python
from typing import List
from asyncio import run

from wrapi.api import query
from wrapi.auth import WrikePermanentTokenAuth
from wrapi.client import async_client
from wrapi.endpoints import folders
from wrapi.entities.folders import Folder
from wrapi.types_.inputs import CustomField, Project


async def main() -> None:
    async with async_client(WrikePermanentTokenAuth("your-auth-token")) as cl:
        create_folder = query(
            cl,
            folders.CreateFolder(
                folder_id="12523623",
                title="New Field",
                custom_fields=(CustomField(id="123456", value="1avagas"),),
                project=Project(custom_status_id="12312415"),
            ),
        )
        
        folder = (await create_folder.as_model(List[Folder]))[0]
        update_folder = query(cl, folders.ModifyFolder(folder_id=folder.id, add_parents=("123456", )))
        
        await update_folder.ignored()


if __name__ == "__main__":
    run(main())
```

What's not implemented yet:
* downloading attachments
* authorization with refresh tokens
* pagination for some methods

What's would be good to add:
* model's automapping based on "kind" field in response
* autogenerating parameters for bodies and queries in base endpoints
