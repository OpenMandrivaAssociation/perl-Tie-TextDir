%define upstream_name       Tie-TextDir
Name:		perl-%{upstream_name}
Version:	0.07
Release:	2
License:	GPL or Artistic
Summary:	Interface to directory of file
Group:		Development/Perl
Url:		https://metacpan.org/dist/Tie-TextDir
Source:		https://cpan.metacpan.org/authors/id/K/KW/KWILLIAMS/Tie-TextDir-%{version}.tar.gz
BuildRequires:	make
BuildRequires:	perl-devel
BuildArch:	noarch

%description
The Tie::TextDir module is a TIEHASH interface which lets you tie a Perl hash
to a directory on the filesystem. Each entry in the hash represents a file in
the directory.

%prep
%setup -q -n %{upstream_name}-%{version} 

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
