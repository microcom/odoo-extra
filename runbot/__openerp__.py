{
    'name': 'Runbot',
    'category': 'Website',
    'summary': 'Runbot',
    'version': '1.2.1',
    'description': "Runbot",
    'author': 'OpenERP SA, Microcom',
    'depends': ['website'],
    'external_dependencies': {
        'python': ['matplotlib'],
    },
    'data': [
        'runbot.xml',
        'res_config_view.xml',
        'security/runbot_security.xml',
        'security/ir.model.access.csv',
        'security/ir.rule.csv',
    ],
    'installable': True,
}
