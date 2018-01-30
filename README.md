# DBBackup

Easy remote (or local) database backup system

It makes backups:
- Monthly
- Weekly
- Daily

Backups to keep can be modified into configuration file.
By default:
- 120 months
- 4 weeks
- 7 days

### Installation

- Clone project:

      git clone https://github.com/estevopaz/DBBackup.git

- System installation (as __root__):

      cd DBBackup
      ./setup.py install

### Configuration

Configuration must be done as __root__:

- Copy configuration file example:

      cd DBBackup
      mkdir /etc/dbbackup
      cp config.yml /etc/dbbackup
      chmod 600 /etc/dbbackup/config.yml
      
- Now just edit the configuration file:

      nano /etc/dbbackup/config.yml
  
### Usage

You can usage the command from terminal manually,
but ideally must be configured into __cron__ for daily execution.

Keep in mind that must be executed by __root__.

    crontab -e
    0 23 * * *  DBBackup

## Notes

Any kind of contribution to the project will be welcome.
