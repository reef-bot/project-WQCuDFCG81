# role_management.py

# Import necessary packages
import discord

# Function to assign a role to a user
async def assign_role(user, role):
    try:
        await user.add_roles(role)
        return True
    except discord.Forbidden:
        print("Bot does not have permission to assign roles.")
        return False

# Function to remove a role from a user
async def remove_role(user, role):
    try:
        await user.remove_roles(role)
        return True
    except discord.Forbidden:
        print("Bot does not have permission to remove roles.")
        return False

# Function to get a list of roles for a user
def get_user_roles(user):
    roles = [role.name for role in user.roles]
    return roles

# Function to get a list of all roles in the server
def get_server_roles(server):
    roles = [role.name for role in server.roles]
    return roles

# Function to create a new role in the server
async def create_role(server, role_name):
    try:
        new_role = await server.create_role(name=role_name)
        return new_role
    except discord.Forbidden:
        print("Bot does not have permission to create roles.")
        return None

# Function to delete a role from the server
async def delete_role(role):
    try:
        await role.delete()
        return True
    except discord.Forbidden:
        print("Bot does not have permission to delete roles.")
        return False