#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
from application import create_app

app = create_app(__name__)
app.config.from_object('config.default')
app.config.from_object('config.production')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Start the Flask App')
    parser.add_argument(
        '--env',
        default='production',
        choices=['production', 'development', 'qa', 'ci'],
        help='Run the server with this configuration and environment'
    )

    args = parser.parse_args()

    if args.env == 'production':
        app.logger.warning('You are using the production config with a '
                           'development server!')
    else:
        app.config.from_object('config.{0}'.format(args.env))

    app.logger.info('Starting "{0}" ({1})'
                    .format(app.config['APP_NAME'], args.env))
    app.run(host=app.config['HOST'], debug=app.config['DEBUG'])
