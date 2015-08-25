policy={JAVA_HOME}/bin/jstatd.all.policy
[ -r ${policy} ] || cat >${policy} <<'POLICY'
grant codebase "file:${JAVA_HOME}/../lib/tools.jar" {
  permission java.security.AllPermission;
};
POLICY


jstatd  -p 18080 -J-Dva.rmi.server.logCalls=true -J-Djava.security.policy=${policy} &
#jstatd  -p 18080 -J-Dva.rmi.server.logCalls=true -J-Djava.security.policy=/usr/java/jdk1.7.0_45/bin/jstatd.all.policy
