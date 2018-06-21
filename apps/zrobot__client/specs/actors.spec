[actor] @dbtype:fs
    """
    Actor for managing 0-robot clients
    """
    method:add
        """
        Add a new 0-robot client
        """
        var:url str,, address of the 0-robot server
        var:name str,, name to give to the client instance
        result:bool, True if client was added

    method:get
        """
        Returns client instance info using the name
        """
        var:name str,, name of the client instance
        result:dict, dict with client info

    method:getService
        """
        Returns service info
        """
        var:robotName str,, name of the client instance
        var:guid str,, service guid
        result:dict, dict with service info

    method:getTask
        """
        Returns task info
        """
        var:robotName str,, name of the client instance
        var:serviceGuid str,, service guid
        var:taskGuid str,, task guid
        result:dict, dict with task info

    method:list
        """
        List all available clients
        """
        result:[], list all available clients name and addresses as a dict

    method:listRobotServices
        """
        List all services in a 0-robot server
        """
        var:name str,, name of the client instance
        result:[], list of service dict containing service info

    method:listRobotTemplates
        """
        List all templates in a 0-robot server
        """
        var:name str,, name of the client instance
        result:[], list of service dict containing template info

