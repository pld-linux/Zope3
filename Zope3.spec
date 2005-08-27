Summary:	An application server and portal toolkit for building Web sites
Summary(es):	Un servidor de aplicaciones y un conjunto de herramientas para la construcción de sitios Web
Summary(pl):	Serwer aplikacji i toolkit portalowy do tworzenia serwisów WWW
Summary(pt_BR):	Um servidor de aplicações e um conjunto de ferramentas para construção de sites Web
Name:		Zope3
Version:	3.1.0
%define		sub_ver c1
Release:	0.%{sub_ver}.0.1
License:	Zope Public License (ZPL)
Group:		Networking/Daemons
Source0:	http://www.zope.org/Products/Zope3/%{version}%{sub_ver}/%{name}-%{version}%{sub_ver}.tgz
# Source0-md5:	e22eeeae5de89c0eea9edabe3f2c3c4d
Source1:	%{name}.init
Source2:	%{name}.sysconfig
Source3:	%{name}.logrotate
URL:		http://dev.zope.org/Zope3
BuildRequires:	python-devel >= 1:2.4.1
BuildRequires:	perl-base
BuildRequires:	rpmbuild(macros) >= 1.213
PreReq:		rc-scripts
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(post,preun):	/sbin/chkconfig
Requires:	expat >= 1.95.7
Requires:	logrotate
Requires:	python >= 2.4.1
Requires:	python-modules >= 2.4.1
Requires:	python-libs >= 2.4.1
Requires:	python-zope-interface = %{epoch}:%{version}-%{release}
%pyrequires_eq	python
Provides:	group(zope)
Provides:	user(zope)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		zope_dir /usr/lib/zope3

%description
The Z Object Programming Environment (Zope) is a free, Open Source
Python-based application server for building high-performance, dynamic
web sites, using a powerful and simple scripting object model and
high-performance, integrated object database.

This project is a redesign of Zope 2 and seeks to improve the Zope development
experience through the use of Interfaces and Components.

%description -l es
Zope es una aplicación basada en Python, Open Source[tm], para la
construcción de sitios dinámicos, usa un modelo de escritura de
guiones poderoso y sencillo. Para instalar la aplicación Zope, instale
ese paquete y después, Zope-server, para un servidor HTTP integrado
simple, Zope-pcgi, para uso con el servidor Apache. Si desea instalar
solamente algunas partes de la aplicación Zope, están diponibles otros
subpaquetes, usted debe instalar éstos en vez de ese RPM.

%description -l pl
Zope (Z Object Programming Environment - Obiektowe ¦rodowisko
Programistyczne Z) jest opartym o Pythona serwerem aplikacji do
tworzenia wysoko wydajnych, dynamicznych serwisów WWW, przy u¿yciu
u¿ytecznego i prostego modelu obiektowego skryptów oraz wysoko
wydajnej zintegrowanej obiektowej bazy danych.

%description -l pt_BR
Zope é uma aplicação baseada em Python, Open Source[tm], para
construção de sites dinâmicos, usando um modelo de scripting poderoso
e simples Para instalar o Zope, instale esse pacote e depois, ou o
Zope-server, para um servidor HTTP integrado simples, ou Zope-pcgi,
para uso com o Apache. Se você quiser instalar apenas algumas partes
do Zope, outros sub-pacotes estão disponíveis, e você deveria instalar
eles ao invés desse RPM.

%package -n python-zope
Summary:	Python packages developed as part of the Zope 3 project
Summary(pl):	Modu³y Pythona rozwijane w projekcie Zope 3
Group:		Development/Tools
Provides:	ZopeInterface
Provides:	python-zope-cachedescriptors
Provides:	python-zope-component
Provides:	python-zope-configuration
Provides:	python-zope-deprecation
Provides:	python-zope-documenttemplate
Provides:	python-zope-event
Provides:	python-zope-exceptions
Provides:	python-zope-hookable
Provides:	python-zope-i18n
Provides:	python-zope-i18nmessageid
Provides:	python-zope-index
Provides:	python-zope-interface
Provides:	python-zope-modulealias
Provides:	python-zope-pagetemplate
Provides:	python-zope-proxy
Provides:	python-zope-publisher
Provides:	python-zope-schema
Provides:	python-zope-security
Provides:	python-zope-server
Provides:	python-zope-structuredtext
Provides:	python-zope-tal
Provides:	python-zope-tales
Provides:	python-zope-testing
Provides:	python-zope-thread
Obsoletes:	ZopeInterface

%description -n python-zope
The "zope" package is a pure namespace package holding packages
developed as part of the Zope 3 project.

Generally, the immediate subpackages of the "zope" package should be
useful and usable outside of the Zope application server. Subpackages
of the "zope" package should have minimal interdependencies, although
most depend on "zope.interface".

%description -n python-zope -l pl
Pakiet "zope" to pakiet czystej przestrzeni nazw przechowuj±cej
pakiety tworzone jako czê¶æ projektu Zope 3.

Ogólnie bezpo¶rednie podpakiety pakietu "zope" powinny byæ przydatne i
u¿ywalne poza serwerem aplikacji Zope. Podpakiety pakietu "zope"
powinny mieæ minimalne zale¿no¶ci wzajemne, chocia¿ wiêkszo¶æ zale¿y
od "zope.interface".

%prep
%setup -q -n Zope-%{version}%{sub_ver}

%build
./configure \
	--prefix=%{zope_dir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_sbindir}} \
	$RPM_BUILD_ROOT{/etc/logrotate.d,/etc/sysconfig,/etc/rc.d/init.d} \
	$RPM_BUILD_ROOT{/var/lib/zope3/main,/var/run/zope3,/var/log/zope3/main} \
	$RPM_BUILD_ROOT%{_sysconfdir}/zope3/main
	
python install.py -q install --skip-build --home "%{zope_dir}" --root "$RPM_BUILD_ROOT"
mv $RPM_BUILD_ROOT%{zope_dir}/lib/python/zope  $RPM_BUILD_ROOT%{py_sitedir}

find $RPM_BUILD_ROOT%{py_sitedir}/zope -name '*.txt' -o -name '*.cfg' | xargs rm

%py_comp $RPM_BUILD_ROOT%{py_sitedir}/zope
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}/zope

ln -sf %{zope_dir}/bin/mkzopeinstance $RPM_BUILD_ROOT%{_sbindir}/mkzope3instance
for f in zconfig zconfig_schema2html zopetest ; do
	ln -sf %{zope_dir}/bin/"$f" $RPM_BUILD_ROOT%{_sbindir}/"$f"3
done
for f in mkzeoinst runzeo zdctl zdrun zeoctl zeopasswd ; do
	ln -sf %{zope_dir}/bin/"$f".py $RPM_BUILD_ROOT%{_sbindir}/"$f"3
done

install %{SOURCE1} $RPM_BUILD_ROOT/etc/rc.d/init.d/zope3
install %{SOURCE2} $RPM_BUILD_ROOT/etc/sysconfig/zope3
install %{SOURCE3} $RPM_BUILD_ROOT/etc/logrotate.d/zope3

touch $RPM_BUILD_ROOT/var/log/zope3/main/event.log
touch $RPM_BUILD_ROOT/var/log/zope3/main/Z2.log


#install -d $RPM_BUILD_ROOT{/var/lib/zope/main,/var/run/zope,/var/log/zope/main} \
#	$RPM_BUILD_ROOT{/etc/logrotate.d,/etc/sysconfig,/etc/rc.d/init.d} \
#	$RPM_BUILD_ROOT{%{_sysconfdir}/zope/main,%{_sbindir}} \
#	$RPM_BUILD_ROOT%{zope_dir}/bin
#
#ln -sfn /usr/bin/python $RPM_BUILD_ROOT%{zope_dir}/bin/python
#
#%{__make} install \
#	INSTALL_FLAGS="--root $RPM_BUILD_ROOT"
#
#mv $RPM_BUILD_ROOT%{zope_dir}/bin/zpasswd.py $RPM_BUILD_ROOT%{_sbindir}/zpasswd
#mv $RPM_BUILD_ROOT%{zope_dir}/skel $RPM_BUILD_ROOT%{_sysconfdir}/zope
#mv $RPM_BUILD_ROOT{%{zope_dir}/import/*,%{_sysconfdir}/zope/skel/import}
#
#rm -rf $RPM_BUILD_ROOT%{zope_dir}/doc
#rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/zope/skel/log
#rm -f $RPM_BUILD_ROOT%{_sysconfdir}/zope/skel/bin/{runzope.bat,zopeservice.py}.in
#
#install %{SOURCE4} $RPM_BUILD_ROOT%{_sbindir}/mkzopeinstance
#install %{SOURCE5} $RPM_BUILD_ROOT%{_sbindir}/mkzeoinstance
#install %{SOURCE6} $RPM_BUILD_ROOT%{_sbindir}/runzope
#install %{SOURCE7} $RPM_BUILD_ROOT%{_sbindir}/zopectl
#install %{SOURCE8} $RPM_BUILD_ROOT%{_sbindir}/installzopeproduct
#

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 112 zope
%useradd -u 112 -d /var/lib/zope/main -s /bin/false -c "Zope User" -g zope zope

%post
/sbin/chkconfig --add zope
if [ ! -f /etc/zope/main/zope.conf ] ; then
	echo "Creating initial 'main' instance..."
	/usr/sbin/mkzope3instance main zope:zope
	echo "Instance created. Listening on 127.0.0.1:8080, initial user: 'zope' with password: 'zope'"
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/zope ]; then
		/etc/rc.d/init.d/zope stop
	fi
	/sbin/chkconfig --del zope
fi

%postun
if [ "$1" = "0" ] ; then
	%userremove zope
	%groupremove zope
fi

%files
%defattr(644,root,root,755)
%doc Zope/doc/*
%attr(754,root,root) /etc/rc.d/init.d/zope3
%attr(755,root,root) %{_sbindir}/*
%dir %{zope_dir}
%dir %{zope_dir}/bin
%attr(755,root,root) %{zope_dir}/bin/*
%{zope_dir}/include
%{zope_dir}/lib
%dir %{zope_dir}/zopeskel
%dir %{zope_dir}/zopeskel/bin
%attr(755,root,root) %{zope_dir}/zopeskel/bin/*
%{zope_dir}/zopeskel/etc
%{zope_dir}/zopeskel/lib
%{zope_dir}/zopeskel/log
%{zope_dir}/zopeskel/var
%{zope_dir}/zopeskel/README.txt
%{py_sitedir}/zope/app
%attr(775,zope,zope) %dir /var/run/zope3
%attr(775,zope,zope) %dir /var/lib/zope3
%attr(775,zope,zope) %dir /var/lib/zope3/main
%attr(775,zope,zope) %dir /var/log/zope3
%attr(775,zope,zope) %dir /var/log/zope3/main
%attr(640,root,root) %dir /etc/zope3
%attr(640,root,root) %dir /etc/zope3/main
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) /etc/logrotate.d/zope3
%attr(640,root,root) /etc/sysconfig/zope3
%ghost /var/log/zope3/main/event.log
%ghost /var/log/zope3/main/Z2.log

%files -n python-zope
%defattr(644,root,root,755)
%{py_sitedir}/zope
%exclude %{py_sitedir}/zope/app
