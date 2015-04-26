__author__ = 'Matthew'

import click
import os
import bbmove


@click.group()
def cli():
    pass


@cli.command()
@click.argument('source', type=click.Path(exists=True))
@click.argument('destination', type=click.Path(exists=True))
@click.option('--quiet', is_flag=True)
def move(source, destination, quiet):
    files = bbmove.search(source)
    for file in files:
        try:
            file = bbmove.Video(file)
        except bbmove.VideoNoMatchException as e:
            continue
        else:
            if quiet or click.confirm('Do you want to move {0}?'.format(file.filename)):
                file.move(destination)
                if os.path.exists(os.path.join(destination, file.folder_tree, file.filename)) and not quiet:
                    click.echo('Moved {0} to {1}'.format(file.filename, file.folder_tree))


@cli.command()
@click.argument('source', type=click.Path(exists=True))
def search(source):
    files = bbmove.search(source)
    click.echo()
    for file in files:
        try:
            file = bbmove.Video(file)
        except bbmove.VideoNoMatchException as e:
            continue
        else:
            click.echo(file.filename)
            click.echo('  Show:        {0}'.format(file.title))
            click.echo('  Season:      {0}'.format(file.season))
            click.echo('  Episode:     {0}'.format(file.episode))
            click.echo('  Destination: {0}'.format(os.path.join(file.folder_tree, file.filename)))