%global octpkg splines

Summary:	Additional spline functions
Name:		octave-splines
Version:	1.3.5
Release:	2
License:	GPLv3+ and Public Domain
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/splines/
Source0:	https://downloads.sourceforge.net/octave/splines-%{version}.tar.gz

BuildRequires:  octave-devel >= 3.6.0

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Additional spline functions.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

