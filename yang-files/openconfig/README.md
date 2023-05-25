# OpenConfig Deviation Files

Contains IPInfusion deviations for OpenConfig yang files. The original OpenConfig
files can be downloaded from https://github.com/openconfig/public.git:

Last Update: Aug.23,2021 (SHA1: ed650bd969afc2eb5f66d60b86b62ffa6fd5fb8e)

```
git clone git@github.com:openconfig/public.git openconfig/
git checkout ed650bd969afc2eb5f66d60b86b62ffa6fd5fb8e
cd openconfig/release/models
```

The openconfig/release/models/wifi directory must be removed, as it has
unwanted deviations.