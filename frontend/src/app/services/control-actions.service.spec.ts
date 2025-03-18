import { TestBed } from '@angular/core/testing';

import { ControlActionsService } from './control-actions.service';

describe('ControlActionsService', () => {
  let service: ControlActionsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ControlActionsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
