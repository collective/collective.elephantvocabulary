{ }:

let
    pkgs = import <nixpkgs> { };
in

with pkgs;

buildEnv {
  name = "buildout-deco-env";
  paths = [
    python27
    python27Packages.recursivePthLoader
    python27Packages.virtualenv
    python27Packages.zc_buildout_nix
  ] ++ lib.attrValues python27.modules;
}
