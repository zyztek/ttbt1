from utilities.database import AccountManager
import getpass

def main():
    print("=== Añadir Cuenta Gmail ===")
    email = input("Email completo (ej: cuenta@gmail.com): ").strip()
    password = getpass.getpass("Contraseña de la cuenta: ").strip()
    recovery = input("Email de recuperación: ").strip()
    
    manager = AccountManager()
    manager.add_account(email, password)
    print(f"✅ Cuenta {email} añadida exitosamente!")

if __name__ == "__main__":
    main()