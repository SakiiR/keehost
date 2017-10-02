from eve import Eve
from .hooks import on_list, init_document_with_acl, on_delete, on_update
from .auth import RolesAuth

app = Eve(auth=RolesAuth, settings="keehost_core/config/config.py")

app.on_pre_GET += on_list
app.on_insert += init_document_with_acl
app.on_delete_item += on_delete
app.on_update += on_update
