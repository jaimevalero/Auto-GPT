"""Wikipedia search integrations."""
from typing import Any, Dict, List, Optional, Tuple, TypedDict, TypeVar

from auto_gpt_plugin_template import AutoGPTPluginTemplate

from .epg_catalog import _epg_catalog_action, _dispatch_generic_action

PromptGenerator = TypeVar("PromptGenerator")


class Message(TypedDict):
    role: str
    content: str


class AutoGPTEPGCatalog(AutoGPTPluginTemplate):
    """
    EPG Catalog search integrations
    """

    def __init__(self):
        super().__init__()
        self._name = "autogpt-epg-catalog"
        self._version = "0.1.0"
        self._description = "Wikipedia search integrations."
        self._description = """ Telefonica's EPG Catalog for actions:          - CRUD Operations for : Github Teams and repositories, permissions management for all of them."""
        #: VmWare Virtual Machines, OpenStack Tenants, Openshift Namespaces, DCIP Jenkins instances , Jira Proyects, Jira Issues, Harbor Proyects,
    def can_handle_on_response(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_response method.
        Returns:
            bool: True if the plugin can handle the on_response method."""
        return False

    def on_response(self, response: str, *args, **kwargs) -> str:
        """This method is called when a response is received from the model."""
        pass

    def can_handle_post_prompt(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_prompt method.
        Returns:
            bool: True if the plugin can handle the post_prompt method."""
        return True

    def can_handle_on_planning(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_planning method.
        Returns:
            bool: True if the plugin can handle the on_planning method."""
        return False

    def on_planning(
        self, prompt: PromptGenerator, messages: List[str]
    ) -> Optional[str]:
        """This method is called before the planning chat completeion is done.
        Args:
            prompt (PromptGenerator): The prompt generator.
            messages (List[str]): The list of messages.
        """
        pass

    def can_handle_post_planning(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_planning method.
        Returns:
            bool: True if the plugin can handle the post_planning method."""
        return False # !!!! TAL VER SERIA UNA BUENA IDEA CAMBIAR ESTO, SI VEMOS QUE LA TAREA TIENE QUE VER CON LO QUE HACE EL PLUGIN

    def post_planning(self, response: str) -> str:
        """This method is called after the planning chat completeion is done.
        Args:
            response (str): The response.
        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_pre_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the pre_instruction method.
        Returns:
            bool: True if the plugin can handle the pre_instruction method."""
        return False

    def pre_instruction(self, messages: List[str]) -> List[str]:
        """This method is called before the instruction chat is done.
        Args:
            messages (List[str]): The list of context messages.
        Returns:
            List[str]: The resulting list of messages.
        """
        pass

    def can_handle_on_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the on_instruction method.
        Returns:
            bool: True if the plugin can handle the on_instruction method."""
        return False

    def on_instruction(self, messages: List[str]) -> Optional[str]:
        """This method is called when the instruction chat is done.
        Args:
            messages (List[str]): The list of context messages.
        Returns:
            Optional[str]: The resulting message.
        """
        pass

    def can_handle_post_instruction(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_instruction method.
        Returns:
            bool: True if the plugin can handle the post_instruction method."""
        return False

    def post_instruction(self, response: str) -> str:
        """This method is called after the instruction chat is done.
        Args:
            response (str): The response.
        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_pre_command(self) -> bool:
        """This method is called to check that the plugin can
        handle the pre_command method.
        Returns:
            bool: True if the plugin can handle the pre_command method."""
        return False # !!! Si se le pasa algo de este estilo, se le podría cambiar el command name command_name, arguments('jira_create_project', {'project_type': '<project_type>', 'project_lead': '<project_lead>', 'project_name': '<project_name>'})

    def pre_command(
        self, command_name: str, arguments: Dict[str, Any]
    ) -> Tuple[str, Dict[str, Any]]:
        """This method is called before the command is executed.
        Args:
            command_name (str): The command name.
            arguments (Dict[str, Any]): The arguments.
        Returns:
            Tuple[str, Dict[str, Any]]: The command name and the arguments.
        """
        pass

    def can_handle_post_command(self) -> bool:
        """This method is called to check that the plugin can
        handle the post_command method.
        Returns:
            bool: True if the plugin can handle the post_command method."""
        return False

    def post_command(self, command_name: str, response: str) -> str:
        """This method is called after the command is executed.
        Args:
            command_name (str): The command name.
            response (str): The response.
        Returns:
            str: The resulting response.
        """
        pass

    def can_handle_chat_completion(
        self,
        messages: list[Dict[Any, Any]],
        model: str,
        temperature: float,
        max_tokens: int,
    ) -> bool:
        """This method is called to check that the plugin can
        handle the chat_completion method.
        Args:         
            messages (Dict[Any, Any]): The messages. messages = [ {'role': 'system', 'content': 'You are FileReaderGP...json.loads'}, {'role': 'system', 'content': 'The current time and...00:19 2023'} ,{'role': 'user', 'content': 'Determine which next...ied above:'} ]
            model (str): The model name.
            temperature (float): The temperature.
            max_tokens (int): The max tokens.
        Returns:
            bool: True if the plugin can handle the chat_completion method."""
        return False

    def handle_chat_completion(
        self,
        messages: list[Dict[Any, Any]],
        model: str,
        temperature: float,
        max_tokens: int,
    ) -> str:
        """This method is called when the chat completion is done.
        Args:
            messages (Dict[Any, Any]): The messages.
            model (str): The model name.
            temperature (float): The temperature.
            max_tokens (int): The max tokens.
        Returns:
            str: The resulting response.
        """
        return None

    def post_prompt(self, prompt: PromptGenerator) -> PromptGenerator:
        """This method is called just after the generate_prompt is called,
            but actually before the prompt is generated.
        Args:
            prompt (PromptGenerator): The prompt generator.
        Returns:
            PromptGenerator: The prompt generator.
        """

        # prompt.add_command(
        #     "epg_catalog",
        #     """ Telefonica's EPG Catalog for actions:          - CRUD Operations for : VmWare Virtual Machines, OpenStack Tenants, Openshift Namespaces, DCIP Jenkins instances , Jira Proyects, Jira Issues, Harbor Proyects, Github Teams and repositories, permissions management for all of them.""",
        #     {"query": "<query>"},
        #     _epg_catalog_action,
        # )
        # change false, true
        # cahnge enum
        # change current user
        prompt.add_command('ask_inventory_information', 
                           'Query inventory information about the infraestructure, users, permissions', 
                           { "search":"<search>" } ,
                             _dispatch_generic_action ) 

        prompt.add_command('github_add_usuario_organización', 
                           'Github. Licencias de github. Añadir usuario a la organization', 
                           { "github_username":"<login>" , "team":"<team_de_licencias>" } ,
                             _dispatch_generic_action ) 
        
        prompt.add_command('github_delete_usuario_organización', 
                           'Github. Licencias de github. Echar a usuario de la organization', 
                           { "github_username":"<login>" } ,
                             _dispatch_generic_action ) 
        
        prompt.add_command('github_add_copilot', 
                           'Github. Licencias de copilot. Habilitar copilot para usuario',
                           { "github_username":"<login>" } ,
                             _dispatch_generic_action ) 
        
        prompt.add_command('github_remove_copilot', 
                           'Github. Licencias de copilot. Deshabilitar copilot para usuario',
                           { "github_username":"<login>" } ,
                             _dispatch_generic_action ) 
        
        prompt.add_command('github_add_user_to_team', 
                           'Github Teams. Añadir miembro a team',
                           { "github_username":"<login>", "team":"<team>" } ,
                             _dispatch_generic_action ) 
        prompt.add_command('github_remove_user_to_team', 
                           'Github Teams. Quitar miembro a team',
                           { "github_username":"<login>", "team":"<team>" } ,
                             _dispatch_generic_action )           


    # - Licencias de de copilot
    #     - Acciones: 
    #         añadir_usuario_team: <github_username> , "copilot"
    #         eliminar_usuario_team: <github_username>, "copilot"    
    # - Teams de github
    #         añadir_usuario_team: <github_username>, <team>
    #         eliminar_usuario_team: <github_username>, <team>    
    # - Repositorios:
    #         crear_repositorio: <nombre_repositorio>
    #         eliminar_repositorio: <nombre_repositorio>
    #         modificar_repositorio: <nombre_repositorio>
    #         añadir tag: <nombre_repositorio>, <tag>
    # - Tokens    
    #         crear_token: <nombre_token>
    #         eliminar_token: <nombre_token>
    #         modificar_token: <nombre_token>
    # - Webapps  (Prisma)
    #         añadir_repo_webapp: "prisma", <nombre_repositorio>




    #     prompt.add_command('create_jira_project', 
    #                        'Crear nuevo proyecto en Jira', 
    #                        { "project_name":"<project_name>" , "project_key":"<project_key>" , "project_lead" : "<user>" } ,
    #                          _dispatch_generic_action ) 
                           
        return prompt
