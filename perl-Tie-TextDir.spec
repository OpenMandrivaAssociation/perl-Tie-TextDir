%define upstream_name       Tie-TextDir
%define upstream_version    0.06

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
License:    GPL or Artistic
Summary:	Interface to directory of file
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Tie/%{upstream_name}-%{upstream_version}.tar.gz
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The Tie::TextDir module is a TIEHASH interface which lets you tie a Perl hash
to a directory on the filesystem. Each entry in the hash represents a file in
the directory.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%files
%defattr(-,root,root)
%doc Changes MANIFEST README
%{_mandir}/*/*
%{perl_vendorlib}/Tie


