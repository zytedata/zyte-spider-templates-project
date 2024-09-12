from spidermon.contrib.scrapy.monitors import (
    ErrorCountMonitor,
    FieldCoverageMonitor,
    FinishReasonMonitor,
    SpiderCloseMonitorSuite,
    UnwantedHTTPCodesMonitor,
)


class CustomSpiderCloseMonitorSuite(SpiderCloseMonitorSuite):
    monitors = [
        ErrorCountMonitor,
        FinishReasonMonitor,
        UnwantedHTTPCodesMonitor,
        FieldCoverageMonitor,
    ]
