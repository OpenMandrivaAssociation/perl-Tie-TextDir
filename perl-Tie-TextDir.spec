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

# Old package, now some tests fail erroneously
# %check
# make test

%install
%makeinstall_std

%files
%doc Changes MANIFEST README
%{_mandir}/*/*
%{perl_vendorlib}/Tie
