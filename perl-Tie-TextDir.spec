%define upstream_name       Tie-TextDir
%define upstream_version    0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
License:	GPL or Artistic
Summary:	Interface to directory of file
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source:		http://www.cpan.org/modules/by-module/Tie/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildArch:	noarch

%description
The Tie::TextDir module is a TIEHASH interface which lets you tie a Perl hash
to a directory on the filesystem. Each entry in the hash represents a file in
the directory.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc Changes MANIFEST README
%{_mandir}/*/*
%{perl_vendorlib}/Tie

%changelog
* Thu Sep 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.60.0-1mdv2010.0
+ Revision: 437398
- use new %%perl_version macro

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.06-5mdv2009.0
+ Revision: 242073
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-3mdv2008.0
+ Revision: 90083
- rebuild


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 0.06-2mdv2007.0
+ Revision: 108428
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Tie-TextDir

* Fri Apr 23 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.06-1mdk
- 0.06

