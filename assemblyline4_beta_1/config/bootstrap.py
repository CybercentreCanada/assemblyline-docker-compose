from assemblyline.odm.models.user_settings import UserSettings
from assemblyline.common.security import get_password_hash
from assemblyline.odm.models.user import User
from assemblyline.common import forge


ADMIN_USER = 'admin'
INITIAL_ADMIN_PASSWORD = 'admin'


if __name__ == '__main__':
    ds = forge.get_datastore()
    if not ds.user.get_if_exists(ADMIN_USER):
        user_data = User({
            "agrees_with_tos": "NOW",
            "classification": "RESTRICTED",
            "name": "Admin user",
            "password": get_password_hash(INITIAL_ADMIN_PASSWORD),
            "uname": ADMIN_USER,
            "type": [ADMIN_USER, "user", "signature_importer"]})
        ds.user.save(ADMIN_USER, user_data)
        ds.user_settings.save(ADMIN_USER, UserSettings())
        print("Initial user setup finished.")
    else:
        print(f"User {ADMIN_USER} already found, system is already setup.")
