from nelsnmp.hostinfo.version import DeviceVersion

# Comware SAMPLES
#
# Comware Platform Software, Software Version 5.20, Release 2112P08
# HPE Comware Platform Software, Software Version 5.20.105, Release 1810P16
# HPE Comware Platform Software, Software Version 7.1.045, Release 2432P06

# ProCurve SAMPLES
#
# ProCurve 516733-B21 6120XG Blade Switch, revision Z.14.58, ROM Z.14.09 (/ws/swbuildm/Z_zinfandel_fip_t4b_qaoff/code/build/vern(Z1.3.6.1.4.1.11.2.3.7.11.107
# ProCurve J9022A Switch 2810-48G, revision N.11.78, ROM N.10.01 (/sw/code/build/bass)
# HP ProCurve 1810G - 24 GE, P.2.24, eCos-2.0, CFE-2.1
# PROCURVE J9028B - PB.03.10

# OfficeConnect SAMPLES
#
# HPE OfficeConnect Switch 1820 48G J9981A, PT.02.08, Linux 3.6.5-45630aff, U-Boot 2012.10-00119-gae4e43bd91 (Aug 31 2018 - 10:12:27)


class HpeVersion(DeviceVersion):

    def _get_version(self):
        for line in self._descriptions:
            if 'ProCurve' in line:
                self.os = 'procurve'
                parts = line.split(',')
                if len(parts) > 1:
                    if 'revision' in parts[1]:
                        self.version = parts[1].replace('revision', "").strip()
                    else:
                        self.version = parts[1].strip()
            elif 'PROCURVE' in line:
                self.os = 'procurve'
                parts = line.split('-')
                if len(parts) > 1:
                    self.version = parts[1].strip()
            elif 'OfficeConnect' in line:
                self.os = 'officeconnect'
                parts = line.split(',')
                if len(parts) > 1:
                    self.version = parts[1].strip()
            elif 'Comware' in line:
                self.os = 'comware'
                parts = line.split(',')
                if len(parts) > 1:
                    if 'Software Version' in parts[1]:
                        self.version = "V " + parts[1].replace('Software Version', "").strip()
                if len(parts) > 2:
                    if 'Release' in parts[2]:
                        self.version += " - R " + parts[2].replace('Release', "").strip()
            # default HP
            elif 'HP' in line:
                parts = line.split(',')
                if len(parts) > 1:
                    self.version = parts[1].strip()
