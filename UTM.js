export const UTM = {
  analyze(name, humanView, universalView) {
    return {
      entity: name,
      humanBelief: humanView,
      universalTruth: universalView,
      mythLevel: humanView.length / universalView.length,
      delta: universalView.filter(x => !humanView.includes(x)),
      corrected: {
        truth: universalView,
        missing: universalView.filter(x => !humanView.includes(x)),
        falseBeliefs: humanView.filter(x => !universalView.includes(x))
      }
    };
  }
};
