  1. relevant packages should all be on head (nuke on archive, build and inst):
    * itktudoss
    * vtkdevide
    * devide: this one is very important, if an old build remains in build and inst, johannes will of course not rewrite its version.
    * setupenvironment (dre checkout)
  1. devide.py should have a DEV release variable (vs X.Y).
  1. Stamp johannes/config.py to update its SVN release.
  1. Nuke inst/devide and re-run johannes.
  1. Run build\_installer. **Remember to nuke devide-re before you begin!**